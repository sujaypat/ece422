%if v.user is None:
      <div class="row">
        <div class="col-xs-8">
%end

          <!-- Search form -->
          <div class="search-well">
            <form action="./search" method="get" class="form-inline">
              <input id="query" type="text" name="q" placeholder="Enter search terms" autofocus class="form-control input-lg search-field">
              <input id="search-btn" type="submit" value="Search" class="btn btn-lg btn-primary">
            </form>
          </div>

%if v.user is None:
        </div>
        <div class="col-xs-4">

          <!-- Login / create account form -->
          <div class="well">
            <form action="./login" method="post" class="form-inline">{{!v.csrfcode}}
              <p>Log in or create an account.</p>
              <div class="form-group form-space">
                <input id="username" name="username" type="text" placeholder="Username" required class="form-control">
              </div>
              <div class="form-group form-space">
                <input id="userpass" name="password" type="password" placeholder="Password" required class="form-control">
              </div>
              <div class="form-group form-more-space">
                <button id="log-in-btn" type="submit" formaction="./login" class="btn btn-default">Login</button>
                <button id="new-account-btn" type="submit" formaction="./create" class="btn btn-default">Create Account</button>
              </div>
            </form>
          </div>

        </div>
      </div>
%end
%rebase base title="Bungle!", v=v
