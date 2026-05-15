import missingPackage from "missing-package";

export default function Home() {
  void missingPackage;

  return (
    <main style={{ padding: "40px", fontFamily: "Arial, sans-serif" }}>
      <h1>Broken Vercel Deployment</h1>
      <p>This deployment intentionally fails during the build.</p>
    </main>
  );
}
