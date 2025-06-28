-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 28, 2025 at 12:46 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `coding`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(50) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `mess` text NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_num`, `mess`, `date`) VALUES
(1, 'first post\r\n', 'firstpost@gmail.com', '123456789', 'hello hello', '2025-06-16 23:37:37'),
(113, 'a', 'a@gmail.com', '3456789876543458998763456', 'gfdgfdgf', '2025-06-24 14:01:18'),
(114, 'a', 'a@gmail.com', '3456789876543458998763456', 'gfdgfdgf', '2025-06-24 18:08:16');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `img_file` varchar(25) NOT NULL,
  `tag_line` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `slug`, `content`, `date`, `img_file`, `tag_line`) VALUES
(1, 'first post', 'first-post', 'first post', '2025-06-28 14:47:18', 'assets/img/about-bg.jpg', 'first post'),
(2, 'second post', 'second-post', 'second post', '2025-06-28 14:49:07', 'assets/img/about-bg.jpg', 'second post'),
(3, 'third post', 'third-post', 'third post', '2025-06-28 14:52:51', 'assets/img/about-bg.jpg', 'third post'),
(4, 'forth post', 'forth-post', 'forth post', '2025-06-28 14:52:51', 'assets/img/about-bg.jpg', 'forth post'),
(5, 'fifth post', 'fifth-post', 'fifth post', '2025-06-28 14:54:09', 'assets/img/about-bg.jpg', 'fifth post'),
(6, 'sixth post', 'sixth-post', 'sixth post', '2025-06-28 14:54:09', 'assets/img/about-bg.jpg', 'sixth post'),
(7, 'seventh post', 'seventh-post', 'seventh post', '2025-06-28 14:54:51', 'assets/img/about-bg.jpg', 'seventh post');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=115;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
