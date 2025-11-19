{
  section2.map((data, index) => (
    <section
      key={index}
      className="relative py-20 px-6 md:px-16 overflow-hidden"
      style={{
        background: data.background || "#EAF5FF",
      }}
    >
      <motion.div
        className="absolute top-[-100px] right-[-100px] w-[300px] h-[300px] rounded-full blur-[100px] opacity-40 z-0"
        style={{
          background: data.glow || "linear-gradient(90deg, #A8D5FF, #CFEAFF)",
        }}
        animate={{
          y: [0, -20, 0],
          scale: [1, 1.1, 1],
        }}
        transition={{ duration: 6, repeat: Infinity }}
      />

      <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-10 relative z-10">
        <div className="text-left md:w-1/2">
          <motion.h1
            className="text-4xl md:text-[42px] font-riot mb-4"
            style={{
              background:
                data.titleColor || "linear-gradient(90deg, #1D5882, #0E75EC)",
              WebkitBackgroundClip: "text",
              color: "transparent",
            }}
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
          >
            {data.title}
          </motion.h1>

          <motion.p
            className="text-[#595959] text-base md:text-lg mb-6"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.9, delay: 0.2 }}
          >
            {data.description}
          </motion.p>

          <ul className="space-y-5">
            {data.features?.map((feature, idx) => (
              <motion.li
                key={idx}
                className="flex items-start gap-3"
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.6, delay: 0.3 + idx * 0.1 }}
              >
                <div
                  className="p-2 rounded-md flex items-center justify-center"
                  style={{
                    background: feature.iconBackground || "#E9F2FF",
                  }}
                >
                  {feature.icon ? (
                    <span className="text-xl">{feature.icon}</span>
                  ) : (
                    <FaCheckCircle className="text-[#0E75EC]" />
                  )}
                </div>
                <div>
                  <h4 className="font-semibold text-[#1D5882] text-lg">
                    {feature.title}
                  </h4>
                  <p className="text-[#595959] text-sm">{feature.text}</p>
                </div>
              </motion.li>
            ))}
          </ul>
        </div>

        <motion.div
          className="md:w-1/2 flex justify-center"
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1, delay: 0.4 }}
        >
          <Image
            src={data.image}
            alt={`${data.title} illustration`}
            width={600}
            height={400}
            className="rounded-xl drop-shadow-xl hover:scale-105 transition-transform duration-500"
            loading="lazy"
          />
        </motion.div>
      </div>
    </section>
  ));
}
