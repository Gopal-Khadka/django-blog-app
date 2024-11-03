export default function About() {
  return (
    <>
      <section className="py-14">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 relative ">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-9">
            <div className="overflow-hidden rounded-lg">
              <img
                src="https://images.pexels.com/photos/1995842/pexels-photo-1995842.jpeg?auto=compress&cs=tinysrgb&w=592&h=481&dpr=1"
                alt="About Us tailwind page"
                className="max-lg:mx-auto object-cover"
                loading="lazy"
              />
            </div>
            <div className="lg:pl-[100px] flex items-center">
              <div className="data w-full">
                <h2 className="font-manrope font-bold text-2xl lg:text-5xl text-white mb-9 max-lg:text-center relative">
                  Empowering Bloggers
                </h2>
                <p className="font-normal md:text-xl leading-8 text-gray-500 max-lg:text-center max-w-2xl mx-auto">
                  Our platform is designed to make blog management effortless
                  for creators and businesses alike. From drafting to
                  publishing, we've developed an intuitive interface that
                  streamlines every step of the content creation process. With a
                  focus on user experience, our tools help you organize,
                  optimize, and grow your blog, all while keeping the technical
                  complexities hidden in the background.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="py-14">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 relative ">
          <div className="grid grid-cols-1 lg:grid-cols-2 lg:gap-9 ">
            <div className="lg:pr-24 flex items-center">
              <div className="w-full">
                <img
                  src="https://pagedone.io/asset/uploads/1702034785.png"
                  loading="lazy"
                  alt="About Us tailwind page"
                  className="block lg:hidden mb-9 mx-auto object-cover"
                />
                <h2 className="font-manrope font-bold text-2xl md:text-4xl lg:text-5xl text-white mb-9 max-lg:text-center">
                  Built By Bloggers,For Bloggers
                </h2>
                <p className="font-normal md:text-xl leading-8 text-gray-500 max-lg:text-center max-w-2xl mx-auto">
                  Established with a vision to foster quality content creation,
                  our mission is to empower bloggers worldwide to share their
                  voice. We believe that great content deserves to be seen and
                  valued, and that’s why we’re dedicated to providing powerful
                  tools that enhance accessibility, engagement, and
                  discoverability. Join a growing community of passionate
                  creators who are turning their ideas into impact with ease and
                  efficiency.
                </p>
              </div>
            </div>
            <div className="img-box ">
              <img
                src="https://pagedone.io/asset/uploads/1702034785.png"
                alt="About Us tailwind page"
                className="hidden lg:block object-cover"
              />
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
