#Legacy API

    /api
    	?method=
    		get_builds
    			params: channels, device, after(int)
    			returns: [{channel, filename, url, changes, md5sum, api_level, timestamp}]
    		get_all_builds
    			params: channels, device, limit(int)
    			returns: [{channel, filename, url, changes, md5sum, api_level, timestamp, incremental}]

The Legacy API is unversioned. This is used for the current version of CyanogenMod updater, and needs to remain in place for old devices.

#Api Version 1

Unless otherwise stated, all parameters are in json. Versioned APIs start with /api/vX, followed by the URI stated below.

URIs might have a symbol after the HTTP verb. Key:

\*: Requires API Key
\#: Requires device ID

##Errors
If an error occurs, the API will return the appropriate HTTP error code, along with a body of {error: message}

##Structure
    /device
      GET:
        params: (none)
        returns: [{device.manufacturer, device.modelname}]
    /device/<name>
      GET:
        params: none
        returns: {device blob}
      PUT: *
        params: {device blob}
        returns: {device blob}
      PATCH: *
        params: {device patch blob}
        returns: {device blob}
      DELETE: *
        params: {}
        returns: {}
    /build
      GET: #
        params: {model}
        returns: [builds for model]
      POST: *
        params: {build blob}
        returns: {}
      PATCH: *
        params: {build patch blob}
        returns: {build blob}
      DELETE: *
        params: {build id}
        returns: {}
    /build/<type>:
      GET: #
        params: {model}
        returns: {builds for model of type}
