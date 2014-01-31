'''
Created on Jan 24, 2014

@author: ghanshyam
'''
#from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponse
#from django.template import Context, loader 
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    '''
    pinintrest = """
<script type="text/javascript" async src="//assets.pinterest.com/js/pinit.js"></script>
		<script type="text/javascript">
(function(d){
    var f = d.getElementsByTagName('SCRIPT')[0], p = d.createElement('SCRIPT');
    p.type = 'text/javascript';
    p.async = true;
    p.src = '//assets.pinterest.com/js/pinit.js';
    f.parentNode.insertBefore(p, f);
}(document));
</script>
		 """
    squerpinit = """
<a data-pin-do="embedUser" href="http://www.pinterest.com/pinterest/" data-pin-scale-width="80" data-pin-scale-height="320" data-pin-board-width="400"></a>
		 """
    return HttpResponse("<head>"+pinintrest+"</head><h1>Hello, world. You're at the main index.<h1>"+squerpinit)
    '''
    return render_to_response('hellodjango/index.html', context_instance=RequestContext(request))
