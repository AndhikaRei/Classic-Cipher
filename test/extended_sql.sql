-- MariaDB dump 10.18  Distrib 10.5.8-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: case_01
-- ------------------------------------------------------
-- Server version	10.5.8-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `case_01`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `case_01` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `case_01`;

--
-- Table structure for table `dosen`
--

DROP TABLE IF EXISTS `dosen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dosen` (
  `id_pembuat_soal` varchar(10) NOT NULL,
  `jabatan` varchar(15) NOT NULL CHECK (`jabatan` in ('Asisten Ahli','Lektor','Lektor Kepala ','Profesor')),
  `id_pt` varchar(10) DEFAULT NULL,
  `id_jurusan` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id_pembuat_soal`),
  KEY `id_pt` (`id_pt`),
  KEY `id_jurusan` (`id_jurusan`),
  CONSTRAINT `dosen_ibfk_1` FOREIGN KEY (`id_pembuat_soal`) REFERENCES `pembuat_soal` (`id_pembuat_soal`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `dosen_ibfk_2` FOREIGN KEY (`id_pt`) REFERENCES `jurusan_perguruan_tinggi` (`id_pt`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `dosen_ibfk_3` FOREIGN KEY (`id_jurusan`) REFERENCES `jurusan_perguruan_tinggi` (`id_jurusan`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dosen`
--

LOCK TABLES `dosen` WRITE;
/*!40000 ALTER TABLE `dosen` DISABLE KEYS */;
INSERT INTO `dosen` (`id_pembuat_soal`, `jabatan`, `id_pt`, `id_jurusan`) VALUES ('Pembuat_01','Profesor','PT-UI','MA'),('Pembuat_02','Asisten Ahli','PT-ITB','BMD'),('Pembuat_03','Lektor Kepala','PT-ITB','TFI'),('Pembuat_04','Lektor','PT-UGM','PSI'),('Pembuat_05','Profesor','PT-IPB','AKN'),('Pembuat_06','Lektor','PT-ITS','GDI');
/*!40000 ALTER TABLE `dosen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jurusan`
--

DROP TABLE IF EXISTS `jurusan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jurusan` (
  `id_jurusan` varchar(10) NOT NULL,
  `nama_jurusan` varchar(50) NOT NULL,
  PRIMARY KEY (`id_jurusan`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jurusan`
--

LOCK TABLES `jurusan` WRITE;
/*!40000 ALTER TABLE `jurusan` DISABLE KEYS */;
INSERT INTO `jurusan` (`id_jurusan`, `nama_jurusan`) VALUES ('AKN','Akuntansi'),('BMD','Teknik Biomedis'),('GDI','Teknik Geodesi'),('MA','Matematika'),('PSI','Psikologi'),('TFI','Teknik Fisika');
/*!40000 ALTER TABLE `jurusan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jurusan_perguruan_tinggi`
--

DROP TABLE IF EXISTS `jurusan_perguruan_tinggi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jurusan_perguruan_tinggi` (
  `id_pt` varchar(10) NOT NULL,
  `id_jurusan` varchar(10) NOT NULL,
  `kuota_penerimaan` int(11) NOT NULL DEFAULT 0,
  `batas_nilai_lulus` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id_pt`,`id_jurusan`),
  KEY `id_jurusan` (`id_jurusan`),
  CONSTRAINT `jurusan_perguruan_tinggi_ibfk_1` FOREIGN KEY (`id_pt`) REFERENCES `perguruan_tinggi` (`id_pt`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `jurusan_perguruan_tinggi_ibfk_2` FOREIGN KEY (`id_jurusan`) REFERENCES `jurusan` (`id_jurusan`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jurusan_perguruan_tinggi`
--

LOCK TABLES `jurusan_perguruan_tinggi` WRITE;
/*!40000 ALTER TABLE `jurusan_perguruan_tinggi` DISABLE KEYS */;
INSERT INTO `jurusan_perguruan_tinggi` (`id_pt`, `id_jurusan`, `kuota_penerimaan`, `batas_nilai_lulus`) VALUES ('PT-IPB','AKN',90,599),('PT-ITB','BMD',30,743),('PT-ITB','TFI',30,727),('PT-ITS','GDI',60,676),('PT-UGM','PSI',80,643),('PT-UI','MA',75,684);
/*!40000 ALTER TABLE `jurusan_perguruan_tinggi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `no_telp_perguruan_tinggi`
--

DROP TABLE IF EXISTS `no_telp_perguruan_tinggi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `no_telp_perguruan_tinggi` (
  `id_pt` varchar(10) NOT NULL,
  `no_telp` varchar(20) NOT NULL,
  PRIMARY KEY (`id_pt`,`no_telp`),
  UNIQUE KEY `no_telp` (`no_telp`),
  CONSTRAINT `no_telp_perguruan_tinggi_ibfk_1` FOREIGN KEY (`id_pt`) REFERENCES `perguruan_tinggi` (`id_pt`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `no_telp_perguruan_tinggi`
--

LOCK TABLES `no_telp_perguruan_tinggi` WRITE;
/*!40000 ALTER TABLE `no_telp_perguruan_tinggi` DISABLE KEYS */;
INSERT INTO `no_telp_perguruan_tinggi` (`id_pt`, `no_telp`) VALUES ('PT-IPB','280515'),('PT-ITB','177013'),('PT-ITB','193945'),('PT-ITS','166671'),('PT-UGM','169134'),('PT-UI','182121'),('PT-UI','186148');
/*!40000 ALTER TABLE `no_telp_perguruan_tinggi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `non_dosen`
--

DROP TABLE IF EXISTS `non_dosen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `non_dosen` (
  `id_pembuat_soal` varchar(10) NOT NULL,
  `tanggal_bergabung` date NOT NULL,
  `spesialisasi` varchar(10) NOT NULL CHECK (`spesialisasi` in ('Mat_IPA','Fisika','Kimia','Biologi','Geografi','Sosiologi','Ekonomi','Mat_Soshum')),
  PRIMARY KEY (`id_pembuat_soal`),
  CONSTRAINT `non_dosen_ibfk_1` FOREIGN KEY (`id_pembuat_soal`) REFERENCES `pembuat_soal` (`id_pembuat_soal`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `non_dosen`
--

LOCK TABLES `non_dosen` WRITE;
/*!40000 ALTER TABLE `non_dosen` DISABLE KEYS */;
INSERT INTO `non_dosen` (`id_pembuat_soal`, `tanggal_bergabung`, `spesialisasi`) VALUES ('Pembuat_07','2015-07-17','Fisika');
/*!40000 ALTER TABLE `non_dosen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pembuat_soal`
--

DROP TABLE IF EXISTS `pembuat_soal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pembuat_soal` (
  `id_pembuat_soal` varchar(10) NOT NULL,
  `nama_pembuat_soal` varchar(50) NOT NULL,
  `email` varchar(30) NOT NULL,
  PRIMARY KEY (`id_pembuat_soal`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pembuat_soal`
--

LOCK TABLES `pembuat_soal` WRITE;
/*!40000 ALTER TABLE `pembuat_soal` DISABLE KEYS */;
INSERT INTO `pembuat_soal` (`id_pembuat_soal`, `nama_pembuat_soal`, `email`) VALUES ('Pembuat_01','Rinaldi Munir','rinaldi@matematika.org'),('Pembuat_02','Satrio Adi Rukmono','satrio@biomedis.org'),('Pembuat_03','Yani Widyani','yani@tekfis.org'),('Pembuat_04','Fariska','fariska@psikologi.org'),('Pembuat_05','Wikan','wikan@akuntasi.org'),('Pembuat_06','Adi Mulyanto','adi@geografi.org'),('Pembuat_07','Rila Mandala','rila@gmail.com');
/*!40000 ALTER TABLE `pembuat_soal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pembuatan_soal`
--

DROP TABLE IF EXISTS `pembuatan_soal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pembuatan_soal` (
  `id_pembuat_soal` varchar(10) NOT NULL,
  `id_soal` varchar(10) NOT NULL,
  PRIMARY KEY (`id_soal`,`id_pembuat_soal`),
  KEY `id_pembuat_soal` (`id_pembuat_soal`),
  CONSTRAINT `pembuatan_soal_ibfk_1` FOREIGN KEY (`id_soal`) REFERENCES `set_soal` (`id_soal`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `pembuatan_soal_ibfk_2` FOREIGN KEY (`id_pembuat_soal`) REFERENCES `pembuat_soal` (`id_pembuat_soal`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pembuatan_soal`
--

LOCK TABLES `pembuatan_soal` WRITE;
/*!40000 ALTER TABLE `pembuatan_soal` DISABLE KEYS */;
INSERT INTO `pembuatan_soal` (`id_pembuat_soal`, `id_soal`) VALUES ('Pembuat_02','BIO_01'),('Pembuat_02','BIO_02'),('Pembuat_05','EK_01'),('Pembuat_05','EK_02'),('Pembuat_01','FI_01'),('Pembuat_07','FI_01'),('Pembuat_01','FI_02'),('Pembuat_07','FI_02'),('Pembuat_06','GEO_01'),('Pembuat_06','GEO_02'),('Pembuat_03','KI_01'),('Pembuat_03','KI_02'),('Pembuat_04','SO_01'),('Pembuat_04','SO_02');
/*!40000 ALTER TABLE `pembuatan_soal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perguruan_tinggi`
--

DROP TABLE IF EXISTS `perguruan_tinggi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `perguruan_tinggi` (
  `id_pt` varchar(10) NOT NULL,
  `nama_pt` varchar(50) NOT NULL,
  `alamat_pt` varchar(255) NOT NULL,
  PRIMARY KEY (`id_pt`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perguruan_tinggi`
--

LOCK TABLES `perguruan_tinggi` WRITE;
/*!40000 ALTER TABLE `perguruan_tinggi` DISABLE KEYS */;
INSERT INTO `perguruan_tinggi` (`id_pt`, `nama_pt`, `alamat_pt`) VALUES ('PT-IPB','Institut Pertanian Bogor','Kampus IPB, Jl. Raya Dramaga, Babakan, Kec. Dramaga, Kota Bogor'),('PT-ITB','Institut Teknologi Bandung','Jl. Ganesha No.10, Lb. Siliwangi, Kecamatan Coblong, Kota Bandung'),('PT-ITS','Institut Teknologi Sepuluh Nopember','Jl. Teknik Kimia, Keputih, Kec. Sukolilo, Kota SBY'),('PT-UGM','Universitas Gadjah Mada','Bulaksumur, Caturtunggal, Kec. Depok, Kabupaten Sleman'),('PT-UI','Universitas Indonesia','Jl. Margonda Raya, Pondok Cina, Kecamatan Beji, Kota Depok');
/*!40000 ALTER TABLE `perguruan_tinggi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pilihan_jurusan`
--

DROP TABLE IF EXISTS `pilihan_jurusan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pilihan_jurusan` (
  `id_pendaftaran` varchar(10) NOT NULL,
  `id_pt` varchar(10) NOT NULL,
  `id_jurusan` varchar(10) NOT NULL,
  `pilihan_ke` int(11) NOT NULL CHECK (`pilihan_ke` in (1,2,3)),
  PRIMARY KEY (`id_pendaftaran`,`id_pt`,`id_jurusan`),
  KEY `id_pt` (`id_pt`),
  KEY `id_jurusan` (`id_jurusan`),
  CONSTRAINT `pilihan_jurusan_ibfk_1` FOREIGN KEY (`id_pt`) REFERENCES `jurusan_perguruan_tinggi` (`id_pt`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `pilihan_jurusan_ibfk_2` FOREIGN KEY (`id_pendaftaran`) REFERENCES `registrasi` (`id_pendaftaran`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `pilihan_jurusan_ibfk_3` FOREIGN KEY (`id_jurusan`) REFERENCES `jurusan_perguruan_tinggi` (`id_jurusan`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pilihan_jurusan`
--

LOCK TABLES `pilihan_jurusan` WRITE;
/*!40000 ALTER TABLE `pilihan_jurusan` DISABLE KEYS */;
INSERT INTO `pilihan_jurusan` (`id_pendaftaran`, `id_pt`, `id_jurusan`, `pilihan_ke`) VALUES ('Daftar_01','PT-ITB','BMD',1),('Daftar_02','PT-ITB','BMD',1),('Daftar_02','PT-ITB','TFI',2),('Daftar_03','PT-ITB','BMD',2),('Daftar_03','PT-ITB','TFI',1),('Daftar_03','PT-ITS','GDI',3),('Daftar_04','PT-IPB','AKN',1),('Daftar_05','PT-IPB','AKN',1),('Daftar_05','PT-UGM','PSI',2),('Daftar_06','PT-IPB','AKN',1);
/*!40000 ALTER TABLE `pilihan_jurusan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `punya_set_soal`
--

DROP TABLE IF EXISTS `punya_set_soal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `punya_set_soal` (
  `id_ujian` varchar(10) NOT NULL,
  `id_soal` varchar(10) NOT NULL,
  PRIMARY KEY (`id_ujian`,`id_soal`),
  KEY `id_soal` (`id_soal`),
  CONSTRAINT `punya_set_soal_ibfk_1` FOREIGN KEY (`id_ujian`) REFERENCES `ujian` (`id_ujian`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `punya_set_soal_ibfk_2` FOREIGN KEY (`id_soal`) REFERENCES `set_soal` (`id_soal`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `punya_set_soal`
--

LOCK TABLES `punya_set_soal` WRITE;
/*!40000 ALTER TABLE `punya_set_soal` DISABLE KEYS */;
INSERT INTO `punya_set_soal` (`id_ujian`, `id_soal`) VALUES ('Saintek_01','BIO_01'),('Saintek_01','FI_01'),('Saintek_01','KI_01'),('Saintek_02','BIO_02'),('Saintek_02','FI_02'),('Saintek_02','KI_02'),('Saintek_03','BIO_01'),('Saintek_03','FI_02'),('Saintek_03','KI_02'),('Soshum_01','EK_01'),('Soshum_01','GEO_01'),('Soshum_01','SO_01'),('Soshum_02','EK_02'),('Soshum_02','GEO_02'),('Soshum_02','SO_02'),('Soshum_03','EK_01'),('Soshum_03','GEO_01'),('Soshum_03','SO_02');
/*!40000 ALTER TABLE `punya_set_soal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registrasi`
--

DROP TABLE IF EXISTS `registrasi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registrasi` (
  `id_pendaftaran` varchar(10) NOT NULL,
  `id_ujian` varchar(10) NOT NULL,
  `tanggal_pendaftaran` date NOT NULL,
  `nilai` int(11) DEFAULT 0,
  PRIMARY KEY (`id_pendaftaran`),
  KEY `id_ujian` (`id_ujian`),
  CONSTRAINT `registrasi_ibfk_1` FOREIGN KEY (`id_ujian`) REFERENCES `ujian` (`id_ujian`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrasi`
--

LOCK TABLES `registrasi` WRITE;
/*!40000 ALTER TABLE `registrasi` DISABLE KEYS */;
INSERT INTO `registrasi` (`id_pendaftaran`, `id_ujian`, `tanggal_pendaftaran`, `nilai`) VALUES ('Daftar_01','Saintek_01','2020-02-12',745),('Daftar_02','Saintek_02','2020-02-22',831),('Daftar_03','Saintek_03','2020-02-17',667),('Daftar_04','Soshum_01','2020-02-13',450),('Daftar_05','Soshum_02','2020-02-25',770),('Daftar_06','Soshum_03','2020-02-01',680);
/*!40000 ALTER TABLE `registrasi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `set_soal`
--

DROP TABLE IF EXISTS `set_soal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `set_soal` (
  `id_soal` varchar(10) NOT NULL,
  `mata_pelajaran` varchar(15) NOT NULL CHECK (`mata_pelajaran` in ('Mat_IPA','Fisika','Kimia','Biologi','Geografi','Sosiologi','Ekonomi','Mat_Soshum')),
  PRIMARY KEY (`id_soal`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `set_soal`
--

LOCK TABLES `set_soal` WRITE;
/*!40000 ALTER TABLE `set_soal` DISABLE KEYS */;
INSERT INTO `set_soal` (`id_soal`, `mata_pelajaran`) VALUES ('BIO_01','Biologi'),('BIO_02','Biologi'),('EK_01','Ekonomi'),('EK_02','Ekonomi'),('FI_01','Fisika'),('FI_02','Fisika'),('GEO_01','Geografi'),('GEO_02','Geografi'),('KI_01','Kimia'),('KI_02','Kimia'),('SO_01','Sosiologi'),('SO_02','Sosiologi');
/*!40000 ALTER TABLE `set_soal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `siswa_sma`
--

DROP TABLE IF EXISTS `siswa_sma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `siswa_sma` (
  `nisn` varchar(10) NOT NULL,
  `id_sma` varchar(10) NOT NULL,
  `nama_depan` varchar(20) NOT NULL,
  `nama_belakang` varchar(20) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `tanggal_lahir` date NOT NULL,
  `alamat_siswa` varchar(255) NOT NULL,
  `id_pendaftaran` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`nisn`),
  UNIQUE KEY `email` (`email`),
  KEY `id_sma` (`id_sma`),
  KEY `id_pendaftaran` (`id_pendaftaran`),
  CONSTRAINT `siswa_sma_ibfk_1` FOREIGN KEY (`id_sma`) REFERENCES `sma` (`id_sma`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `siswa_sma_ibfk_2` FOREIGN KEY (`id_pendaftaran`) REFERENCES `registrasi` (`id_pendaftaran`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `siswa_sma`
--

LOCK TABLES `siswa_sma` WRITE;
/*!40000 ALTER TABLE `siswa_sma` DISABLE KEYS */;
INSERT INTO `siswa_sma` (`nisn`, `id_sma`, `nama_depan`, `nama_belakang`, `email`, `tanggal_lahir`, `alamat_siswa`, `id_pendaftaran`) VALUES ('0012236441','SMA_01','Reihan','Andhika','andhikareihan349@gmail.com','2001-05-02','JL Panglima Sudirman no 27','Daftar_01'),('0012236442','SMA_02','Kinantan','Arya','kinantanABC@gmail.com','2001-03-02','JL Gajah Mada no 28','Daftar_02'),('0012236443','SMA_03','Andrew',NULL,'andrew@gmail.com','2001-05-17','JL Teuku Umar no 29','Daftar_03'),('0012236444','SMA_04','Muhammad','Bintang','mbintang99@gmail.com','2001-01-03','JL DR Wahidin no 22','Daftar_04'),('0012236445','SMA_05','Ridho','Daffasyah','ridho@gmail.com','2000-03-01','JL Kadipaten no 40','Daftar_05'),('0012236446','SMA_01','Rezi',NULL,'rezi66@gmail.com','2002-11-02','JL Dago no 12','Daftar_06'),('0012236447','SMA_02','Naruto','Uzumaki','nartoHokage@gmail.com','2000-07-17','JL Konoha no 11',NULL),('0012236448','SMA_03','Sasuke','Uchiha','saske124@gmail.com','2000-08-19','JL Ninjamu no 100',NULL);
/*!40000 ALTER TABLE `siswa_sma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sma`
--

DROP TABLE IF EXISTS `sma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sma` (
  `id_sma` varchar(10) NOT NULL,
  `nama_sma` varchar(50) NOT NULL,
  `alamat_sma` varchar(255) NOT NULL,
  PRIMARY KEY (`id_sma`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sma`
--

LOCK TABLES `sma` WRITE;
/*!40000 ALTER TABLE `sma` DISABLE KEYS */;
INSERT INTO `sma` (`id_sma`, `nama_sma`, `alamat_sma`) VALUES ('SMA_01','SMAN 8 Jakarta','Jl. Taman Bukit Duri No.2, Bukit Duri, Kec. Tebet, Kota Jakarta Selatan'),('SMA_02','SMAN 3 Bandung','Jl. Belitung No.8, Merdeka, Kec. Sumur Bandung, Kota Bandung'),('SMA_03','SMAN 5 Surabaya','Jl. Kusuma Bangsa No.21, Ketabang, Kec. Genteng, Kota SBY'),('SMA_04','SMA Pribadi Bandung','Jl. PH.H. Mustofa No.41, Neglasari, Kec. Cibeunying Kaler, Kota Bandung'),('SMA_05','SMAN 1 Bojonegoro','Jl. Panglima Sudirman No.28, Kepatihan, Kec. Bojonegoro, Kabupaten Bojonegoro');
/*!40000 ALTER TABLE `sma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status_perguruan_tinggi`
--

DROP TABLE IF EXISTS `status_perguruan_tinggi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `status_perguruan_tinggi` (
  `id_pt` varchar(10) NOT NULL,
  `tahun` int(11) NOT NULL,
  `jumlah_mahasiswa` int(11) NOT NULL DEFAULT 0,
  `jumlah_dosen` int(11) NOT NULL DEFAULT 0,
  `akreditasi` varchar(20) NOT NULL CHECK (`akreditasi` in ('Baik','Sangat Baik','Unggul','Tidak Terakreditasi')),
  PRIMARY KEY (`id_pt`,`tahun`),
  CONSTRAINT `status_perguruan_tinggi_ibfk_1` FOREIGN KEY (`id_pt`) REFERENCES `perguruan_tinggi` (`id_pt`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status_perguruan_tinggi`
--

LOCK TABLES `status_perguruan_tinggi` WRITE;
/*!40000 ALTER TABLE `status_perguruan_tinggi` DISABLE KEYS */;
INSERT INTO `status_perguruan_tinggi` (`id_pt`, `tahun`, `jumlah_mahasiswa`, `jumlah_dosen`, `akreditasi`) VALUES ('PT-IPB',2020,8821,132,'Tidak Terakreditasi'),('PT-IPB',2021,8725,129,'Unggul'),('PT-ITB',2019,9132,112,'Unggul'),('PT-ITB',2020,9337,114,'Unggul'),('PT-ITB',2021,9657,121,'Unggul'),('PT-ITS',2020,8723,167,'Unggul'),('PT-ITS',2021,8943,187,'Unggul'),('PT-UGM',2020,12231,207,'Baik'),('PT-UGM',2021,12231,223,'Unggul'),('PT-UI',2020,13321,123,'Sangat Baik'),('PT-UI',2021,13741,123,'Unggul');
/*!40000 ALTER TABLE `status_perguruan_tinggi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ujian`
--

DROP TABLE IF EXISTS `ujian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ujian` (
  `id_ujian` varchar(10) NOT NULL,
  `id_sma` varchar(10) NOT NULL,
  `tanggal_ujian` date NOT NULL,
  PRIMARY KEY (`id_ujian`),
  KEY `id_sma` (`id_sma`),
  CONSTRAINT `ujian_ibfk_1` FOREIGN KEY (`id_sma`) REFERENCES `sma` (`id_sma`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ujian`
--

LOCK TABLES `ujian` WRITE;
/*!40000 ALTER TABLE `ujian` DISABLE KEYS */;
INSERT INTO `ujian` (`id_ujian`, `id_sma`, `tanggal_ujian`) VALUES ('Saintek_01','SMA_01','2020-04-12'),('Saintek_02','SMA_01','2020-04-13'),('Saintek_03','SMA_02','2020-04-12'),('Soshum_01','SMA_01','2020-04-12'),('Soshum_02','SMA_03','2020-04-14'),('Soshum_03','SMA_04','2020-04-14');
/*!40000 ALTER TABLE `ujian` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-08 18:20:12
