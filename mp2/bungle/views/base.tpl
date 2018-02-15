<!DOCTYPE html>
<html>
  <head>
    <title>{{title}}</title>
    <link href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
    <style>
      .navbar-inner {
          float: none;
          margin: 0 auto;
          display: table;
          table-layout: fixed;
      }
      .container {
          max-width: none !important;
          width: 800px;
          min-width: 800px;
      }
      .navbar { margin: 0; }
      .main { margin-top: 15px; }
      #logged-in-user { font-weight: bold; }
      .navbar-inverse form { color: #999; }
      h3 { margin-top: 0px; }
      h4 { margin-top: 5px; }
      .search-well {
          width: 475px;
          margin: 60px auto 60px auto;
          text-align: center;
      }
      .search-field { width: 300px; }
      .form-space { margin: 5px 0; }
      .form-more-space { margin: 15px 0 5px 0; }
      .well p { margin: 0 0 5px 0; }
      #query-lbl { color: red; }
      #searchcontrol { margin-bottom: 15px; }
    </style>
    <script>
      function applyDefenses(){
        $('#location').val(document.location);
        $('#setdefenses').submit();
      }
      $(function(){
        $('#xssdefense').change(applyDefenses);
        $('#csrfdefense').change(applyDefenses);
      });
    </script>
  </head>
  <body>

    <!-- Defense selector navbar -->
    <div class="navbar navbar-default navbar-static-top">
      <div class="navbar-inner">
        <form id="setdefenses" action="./setdefenses" method="post" class="navbar-form">
          <div class="form-group">
            <label for="csrfdefense">CSRF:</label>
            <select name="csrfdefense" id="csrfdefense" style="width:auto" class="form-control input-sm">{{!v.defenses.csrfoptions}}</select>
            <label for="xssdefense">XSS:</label>
            <select name="xssdefense" id="xssdefense" style="width:auto" class="form-control input-sm">{{!v.defenses.xssoptions}}</select>&nbsp;
            <input id="location" name="location" type="hidden">
          </div>
        </form>
      </div>
    </div>

    <!-- Bungle navbar -->
    <div class="navbar navbar-inverse navbar-static-top">
      <div class="container">    
        <div class="navbar-header"> 
          <a id="bungle-lnk" class="navbar-brand" href="./">Bungle!</a>
        </div>
        <div class="nav navbar-nav navbar-right">
%if v.user is not None:
          <!-- Logout button -->
          <form action="./logout" method="post" class="navbar-form form-inline">{{!v.csrfcode}}
            Logged in as <span id="logged-in-user">{{v.user.username}}</span>.
            <input id="log-out-btn" type="submit" value="Log out" class="btn btn-link navbar-link">
          </form>
%else:
          <p class="navbar-text">
            Not logged in.
          </p>
%end        
        </div>
      </div>
    </div>

    <div class="container main">

%include
    </div>
  </body>
</html>
