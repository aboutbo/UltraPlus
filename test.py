#!/usr/bin/env python
#coding=utf8
from burp import IBurpExtender
from burp import IHttpListener
from burp import IHttpRequestResponse
from burp import IResponseInfo
import urllib2
import ssl
import requests


# Class BurpExtender (Required) contaning all functions used to interact with Burp Suite API
class BurpExtender(IBurpExtender, IHttpListener):

    # define registerExtenderCallbacks: From IBurpExtender Interface
    def registerExtenderCallbacks(self, callbacks):

        # keep a reference to our callbacks object (Burp Extensibility Feature)
        self._callbacks = callbacks
        # obtain an extension helpers object (Burp Extensibility Feature)
        # http://portswigger.net/burp/extender/api/burp/IExtensionHelpers.html
        self._helpers = callbacks.getHelpers()
        # set our extension name that will display in Extender Tab
        self._callbacks.setExtensionName("test proxy")
        # register ourselves as an HTTP listener
        callbacks.registerHttpListener(self)
        print('success!\nMade by xiwu')

    # define processHttpMessage: From IHttpListener Interface
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):

        # determine what tool we would like to pass though our extension:
        if toolFlag == 4:  #if tool is Proxy Tab or repeater
            # determine if request or response: only handle responses
            if messageIsRequest:
                # get byte instance
                request = messageInfo.getRequest()
                # get Response from IHttpRequestResponse instance
                analyzedRequest = self._helpers.analyzeRequest(
                    messageInfo)  # returns IResponseInfo
                headers = analyzedRequest.getHeaders()
                url = analyzedRequest.getUrl()
                proxy = {
                    'http': 'http://127.0.0.1:80',
                    'https': 'https://127.0.0.1:80',
                }

                # httpproxy_handler = urllib2.ProxyHandler(proxy)
                # opener = urllib2.build_opener(httpproxy_handler)
                # context = ssl._create_unverified_context()
                # urllib2.install_opener(opener)

                if headers[0].startswith('GET'):
                    try:
                        # url = self._helpers.bytesToString(url)
                        # pre_request = urllib2.Request(url)
                        # response = urllib2.urlopen(pre_request, context=context)
                        # print(response.read())
                        requests.get(str(url), timeout=3, verify=False, proxies=proxy)
                    except Exception as e:
                        print(e)

                body = request[analyzedRequest.getBodyOffset():]
                body_string = body.tostring()

                new_body = self._helpers.bytesToString(body_string)

                messageInfo.setRequest(
                    self._helpers.buildHttpMessage(headers, new_body))