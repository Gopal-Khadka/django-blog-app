import Button from "./Button";

const NavBar = () => {
  return (
    <nav className="bg-slate-600 display flex justify-between px-3 py-2 items-center">
      <div className="font-semibold text-2xl">DesiBlogs</div>
      <ul className="flex gap-3">
        <li>Home</li>
        <li>About</li>
        <li>Contact</li>
      </ul>
      <div>
        <Button text="Login/SignUp"/>
      </div>
    </nav>
  );
};
export default NavBar;