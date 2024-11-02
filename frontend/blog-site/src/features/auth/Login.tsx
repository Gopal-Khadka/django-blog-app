import { useState } from "react";

const Login = () => {
  const [isSignUp, setisSignUp] = useState(false);
  const loginState = isSignUp ? "Sign Up" : "Log In";
  return (
    <div className="flex flex-col justify-center items-center ">
      <div className="mx-auto flex w-full flex-col justify-center px-5 pt-0  md:max-w-[50%]  lg:max-w-[50%] lg:px-6">
        <div className="my-auto mb-auto flex flex-col min-w-[300px] max-w-[450px] mx-auto md:max-w-[450px] lg:max-w-[450px]">
          <p className="text-[32px] font-bold text-white text-center">
            {loginState} Form
          </p>
          <p className="mb-2.5 mt-2.5 font-normal text-zinc-400">
            Enter your email and password to{" "}
            <span className="lowercase">{loginState}</span>!
          </p>
          <div className="mt-8">
            <form className="pb-2" method="POST">
              <input type="hidden" name="provider" value="google" />
              <button
                className="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground h-10 px-4 w-full py-6 text-white"
                type="submit"
              >
                <span className="mr-2">
                  <img src="./google.svg" className="h-14 w-14" />
                </span>
                <span>Google</span>
              </button>
            </form>
          </div>
          <div className="relative my-4">
            <div className="relative flex items-center py-1">
              <div className="grow border-t border-zinc-700"></div>
              <div className="grow border-t border-zinc-700"></div>
            </div>
          </div>
          <div>
            <form className="mb-2">
              <div className="grid gap-2">
                <div className="grid gap-1">
                  <label className="text-white" htmlFor="email">
                    Email
                  </label>
                  <input
                    className="mr-2.5 mb-2 h-full min-h-[44px] w-full rounded-lg border border-zinc-200 bg-white px-4 py-3 text-sm font-medium focus:outline-0 dark:border-zinc-800 dark:bg-transparent text-white placeholder:text-zinc-400"
                    id="email"
                    placeholder="name@example.com"
                    type="email"
                    autoComplete="email"
                    autoCorrect="off"
                    name="email"
                  />
                  <label className="text-white" htmlFor="password">
                    Password
                  </label>
                  <input
                    id="password"
                    placeholder="Password"
                    type="password"
                    autoComplete="current-password"
                    className="mr-2.5 mb-2 h-full min-h-[44px] w-full rounded-lg border border-zinc-200 bg-white px-4 py-3 text-sm font-medium focus:outline-0 dark:border-zinc-800 dark:bg-transparent text-white placeholder:text-zinc-400"
                    name="password"
                  />
                </div>
                <button
                  className="whitespace-nowrap ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 mt-2 flex h-[unset] w-full items-center justify-center rounded-lg px-4 py-2 text-sm font-medium"
                  type="submit"
                >
                  {loginState}
                </button>
              </div>
            </form>

            <p>
              <a
                className="font-medium text-sm cursor-pointer text-green-500"
                onClick={() => setisSignUp((prev) => !prev)}
              >
                Don't have an account? {isSignUp ? "Log in" : "Sign up"}
              </a>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
