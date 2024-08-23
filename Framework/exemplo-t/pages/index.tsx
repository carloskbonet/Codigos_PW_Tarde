import { checkToken } from "@/services/tokenConfig";
import { getCookie } from "cookies-next";
import styles from "@/styles/home.module.css"
import { useState, useEffect } from "react";

export default function Home() {

  const [data, setData]: any = useState(undefined);

  async function fetchData() {
    try {
      const response = await fetch(`/api/action/movie/select`, {
        method: 'GET'
      });

      const responseJson = await response.json();

      setData(responseJson.data);
    }
    catch (err) {
      console.log(err);
    }
  }

  useEffect(() => {
    fetchData();
  }, [])

  function exibirFilmes() {
    console.log(data);
  }


  return (
    <main id={styles.main} className="flex min-h-screen flex-col">
      <button onClick={exibirFilmes}> Printar os filmes </button>




      {/* Barra superior de navegação */}
      <nav className={styles.navBar}>
        <img src="/pipoca.png" className={styles.icon} alt="" />

        <div className={styles.searchContainer}>
          <input type="text" className={styles.searchBar} />
          <button className={styles.send}>Enviar</button>
        </div>

        <button className={styles.logoutBtn}>Logout</button>

      </nav>

      {/* Container principal. Ele vai conter o GRID */}
      <div className={styles.mainContainer}>

        {/* Painel esquerdo */}
        <div className={styles.leftContainer}>

        </div>

        {/* Painel direito */}
        <div className={styles.rightContainer}>

          {data != undefined && data instanceof Array ?

            data.map(movie => (
              <div className={styles.card}>
                <img src="/card.jfif" className={styles.cardImg} alt="" />
                <div className={styles.cardInfos}>
                  <h2>{movie.name}</h2>
                  <p>{movie.releaseDate}</p>
                  <p>Generos do Filme</p>
                  <p>{movie.description}</p>
                </div>
              </div>
            ))

            :

            <p>No movies Found</p>

          }


        </div>

      </div>

    </main>
  );
}



export function getServerSideProps({ req, res }: any) {
  try {
    const token = getCookie('authorization', { req, res });

    if (!token) {
      throw new Error('Invalid Token');
    }
    else {
      checkToken(token);
    }

    return {
      props: {}
    }

  }
  catch (err) {
    return {
      redirect: {
        permanent: false,
        destination: '/user/login'
      },
      props: {}
    }
  }
}