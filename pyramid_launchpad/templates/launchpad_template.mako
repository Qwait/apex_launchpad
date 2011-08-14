<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
<title></title>
<link rel="stylesheet" href="${request.static_url('pyramid_apex:static/css/apex_forms.css')}" type="text/css" media="screen" charset="utf-8" />
<link rel="stylesheet" href="${request.static_url('pyramid_launchpad:static/css/base.css')}" type="text/css" media="screen" charset="utf-8" />
</head>
<body>

<div class="wrap">
 <div style="width: 340; height: 146px; background: #000;"></div>
 ${launch_settings('blurb')}
 ${form.render()|n}
</div>

</body>
</html>
