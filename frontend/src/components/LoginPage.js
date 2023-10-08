import React from 'react';  
  
function LoginPage() {  
  return (  
    <div className="container">  
      <div className="row justify-content-center">  
        <div className="col-md-6">  
          <div className="card">  
            <div className="card-header">Login</div>  
            <div className="card-body">  
              <form>  
                <div className="form-group mb-3">  
                  <label>Email address</label>  
                  <input type="email" className="form-control" placeholder="Enter email" />  
                </div>  
  
                <div className="form-group mb-3">  
                  <label>Password</label>  
                  <input type="password" className="form-control" placeholder="Enter password" />  
                </div>  
  
                <div className="form-group mb-3">  
                  <div className="custom-control custom-checkbox">  
                    <input type="checkbox" className="custom-control-input" id="customCheck1" />  
                    <label className="custom-control-label" htmlFor="customCheck1">Remember me</label>  
                  </div>  
                </div>  
  
                <button type="submit" className="btn btn-primary btn-block">Submit</button>  
                <p className="forgot-password text-right">  
                  Forgot <a href="#">password?</a>  
                </p>  
              </form>  
            </div>  
          </div>  
        </div>  
      </div>  
    </div>  
  );  
}  
  
export default LoginPage;  
