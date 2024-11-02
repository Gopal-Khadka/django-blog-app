import MainLayout from "./layouts/MainLayout";
import Login from "./features/auth/Login";
function App() {
  return (
    <MainLayout>
      <div className="px-5 py-3 mt-20 md:mt-14">
        <Login />
      </div>
    </MainLayout>
  );
}

export default App;
