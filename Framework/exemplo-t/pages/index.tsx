import { checkToken } from "@/services/tokenConfig";
import { deleteCookie, getCookie } from "cookies-next";
import styles from "@/styles/home.module.css"
import { useState, useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/router";
import Navbar from "@/components/Navbar";

export default function Home() {
  const router = useRouter();
  const [data, setData]: any = useState(undefined);
  // Constante para salvar todos os filmes
  const [saveData, setSaveData]: Array<any> = useState(undefined);

  // Constante para salvar o texto da barra de pesquisa
  const [name, setName] = useState('');

  function searchFilter(array: any, text: string) {
    if (text == '') {
      return array;
    }
    else {
      return array.filter((singleMovie: any) => singleMovie.name.toLowerCase().includes(text.toLowerCase()));
    }
  }

  function formSubmit(event: any) {
    event.preventDefault();
    try {

      const filteredMovies = searchFilter(saveData, name);

      setData(filteredMovies);

    }
    catch (err) {
      console.log(err);
    }
  }


  async function fetchData() {
    try {
      const response = await fetch(`/api/action/movie/select`, {
        method: 'GET'
      });

      const responseJson = await response.json();

      setData(responseJson.data);
      setSaveData(responseJson.data);
    }
    catch (err) {
      console.log(err);
    }
  }

  useEffect(() => {
    fetchData();
  }, [])


  function movieClick(movieName: string) {
    router.push(`/movie/` + movieName);
  }

  function dateFormat(_date: string) {
    // data esperada : 2024-09-12T17:19
    const [date, time] = _date.split("T");
    const [year, month, day] = date.split("-");

    return `${day}/${month}/${year}`;
  }


  return (
    <main id={styles.main} className="flex min-h-screen flex-col">

      {/* Barra superior de navegação */}

      <Navbar>

        <form className={styles.searchContainer} onSubmit={formSubmit} >
          <input type="text" className={styles.searchBar} onChange={(e) => { setName(e.target.value) }} />
          <button className={styles.send}>Enviar</button>
        </form>

      </Navbar>




      {/* Container principal. Ele vai conter o GRID */}
      <div className={styles.mainContainer}>

        {/* Painel esquerdo */}
        <div className={styles.leftContainer}>

        </div>

        {/* Painel direito */}
        <div className={styles.rightContainer}>

          {data != undefined && data instanceof Array ?

            data.map(movie => (
              <div onClick={() => { movieClick(movie.name) }} className={styles.card}>
                <img src={movie.imageURL} className={styles.cardImg} alt="" />
                <div className={styles.cardInfos}>
                  <h2>{movie.name}</h2>
                  <p>{dateFormat(movie.releaseDate)}</p>
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