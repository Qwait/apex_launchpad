<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
<title>${launch_settings('title')}</title>
<link rel="stylesheet" href="${request.static_url('pyramid_apex:static/css/apex_forms.css')}" type="text/css" media="screen" charset="utf-8" />
<link rel="stylesheet" href="${request.static_url('pyramid_launchpad:static/css/base.css')}" type="text/css" media="screen" charset="utf-8" />
% if launch_settings('meta_description'):
<meta name="description" content="${launch_settings('meta_description')}" />
% endif
% if launch_settings('meta_keywords'):
<meta name="keywords" content="${launch_settings('meta_keywords')}" />
% endif

% if launch_settings('og.title'):
<meta property="og:title" content="${launch_settings('og.title')}" />
% endif
% if launch_settings('og.type'):
<meta property="og:type" content="${launch_settings('og.type')}" />
% endif
% if launch_settings('og.url'):
<meta property="og:url" content="${launch_settings('og.url')}" />
% endif
% if launch_settings('og.image'):
<meta property="og:image" content="${launch_settings('og.image')}" />
% endif
% if launch_settings('og.site_name'):
<meta property="og:site_name" content="${launch_settings('og.site_name')}" />
% endif
% if launch_settings('og.fb_admins'):
<meta property="fb:admins" content="${launch_settings('fb_admins')}" />
% endif

% if launch_settings('google_analytics'):
<script type="text/javascript">
var _gaq=_gaq||[];_gaq.push(["_setAccount","${launch_settings('google_analytics')}"]);_gaq.push(["_trackPageview"]);_gaq.push(["_trackPageLoadTime"]);(function(){var a=document.createElement("script");a.type="text/javascript";a.async=!0;a.src=("https:"==document.location.protocol?"https://ssl":"http://www")+".google-analytics.com/ga.js";var b=document.getElementsByTagName("script")[0];b.parentNode.insertBefore(a,b)})();
</script>
% endif

</head>
<body>
<!-- background_image -->

<div class="wrap">
 <div style="width: 350; height: 150px; background: #000;">
% if launch_settings('form_image'):
<img src="${launch_settings('form_image')}" width="350" height="150" />
% endif
 </div>
 ${launch_settings('blurb')}
% if action == 'index':
 ${form.render()|n}
% else:
Thank you
% endif

<div style="float:left;">
<g:plusone href="${launch_settings('og.url')}"></g:plusone>
</div>
<div style="float:left;">
<a href="http://twitter.com/share?url=${launch_settings('og.url')}&text=${launch_settings('twitter_description')}" class="twitter-share-button" data-count="horizontal">Tweet</a>
</div>
<div style="float:left;">
<div id="fb-root"></div>
<fb:like href="${launch_settings('og.url')}" width="150" show_faces="false" font="" layout="button_count" action="recommend"></fb:like>
</div>
<div style="clear:both;"></div>
</div>

</div>
<script type="text/javascript">
var a=["https://apis.google.com/js/plusone.js","http://platform.twitter.com/widgets.js","http://connect.facebook.net/en_US/all.js#appId=${launch_settings('facebook_appid')}&xfbml=1"];for(script_index in a){var b=document.createElement("script");b.type="text/javascript";b.async=!0;b.src=a[script_index];var c=document.getElementsByTagName("script")[0];c.parentNode.insertBefore(b,c)};
</script>
</body>
</html>
