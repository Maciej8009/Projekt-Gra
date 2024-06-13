-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Cze 13, 2024 at 02:26 AM
-- Wersja serwera: 10.4.28-MariaDB
-- Wersja PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gra3`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `store`
--

CREATE TABLE `store` (
  `ProductID` int(11) NOT NULL,
  `ProductName` varchar(32) NOT NULL,
  `StonePrice` int(11) NOT NULL DEFAULT 0,
  `WoodPrice` int(11) NOT NULL DEFAULT 0,
  `MoneyPrice` int(11) NOT NULL DEFAULT 0,
  `IronPrice` int(11) NOT NULL DEFAULT 0,
  `DiamondsPrice` int(11) NOT NULL DEFAULT 0,
  `Image` longblob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `store`
--

INSERT INTO `store` (`ProductID`, `ProductName`, `StonePrice`, `WoodPrice`, `MoneyPrice`, `IronPrice`, `DiamondsPrice`, `Image`) VALUES
(0, 'Axe', 0, 0, 1000, 0, 0, NULL),
(1, 'Pickaxe', 0, 1000, 10000, 0, 0, NULL),
(2, 'Better Pickaxe', 10000, 15000, 20000, 0, 0, NULL),
(3, 'Drill', 20000, 25000, 30000, 10000, 0, NULL);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `userinventory`
--

CREATE TABLE `userinventory` (
  `UserID` int(11) NOT NULL,
  `Money` int(11) NOT NULL DEFAULT 2000,
  `Wood` int(11) NOT NULL DEFAULT 0,
  `Stone` int(11) NOT NULL DEFAULT 0,
  `Diamonds` int(11) NOT NULL DEFAULT 0,
  `Iron` int(11) NOT NULL DEFAULT 0,
  `Axe` tinyint(1) NOT NULL DEFAULT 0,
  `Pickaxe` tinyint(1) NOT NULL DEFAULT 0,
  `Better Pickaxe` tinyint(1) NOT NULL DEFAULT 0,
  `Drill` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userinventory`
--

INSERT INTO `userinventory` (`UserID`, `Money`, `Wood`, `Stone`, `Diamonds`, `Iron`, `Axe`, `Pickaxe`, `Better Pickaxe`, `Drill`) VALUES
(28, 1000, 0, 0, 0, 0, 1, 0, 0, 0),
(29, 2008, 6, 0, 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `usermain`
--

CREATE TABLE `usermain` (
  `UserID` int(11) NOT NULL,
  `UserNickName` varchar(20) NOT NULL,
  `UserPassword` varchar(128) NOT NULL,
  `UserEmail` varchar(64) NOT NULL,
  `UserScore` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usermain`
--

INSERT INTO `usermain` (`UserID`, `UserNickName`, `UserPassword`, `UserEmail`, `UserScore`) VALUES
(28, 'Admin', 'e86f78a8a3caf0b60d8e74e5942aa6d86dc150cd3c03338aef25b7d2d7e3acc7', 'Admin@wp.pl', 0),
(29, 'Admin1', 'e86f78a8a3caf0b60d8e74e5942aa6d86dc150cd3c03338aef25b7d2d7e3acc7', 'Admin1@wp.pl', 10);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `store`
--
ALTER TABLE `store`
  ADD PRIMARY KEY (`ProductID`);

--
-- Indeksy dla tabeli `userinventory`
--
ALTER TABLE `userinventory`
  ADD KEY `UserID` (`UserID`);

--
-- Indeksy dla tabeli `usermain`
--
ALTER TABLE `usermain`
  ADD PRIMARY KEY (`UserID`),
  ADD UNIQUE KEY `UserNickName` (`UserNickName`),
  ADD UNIQUE KEY `UserEmail` (`UserEmail`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `store`
--
ALTER TABLE `store`
  MODIFY `ProductID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `usermain`
--
ALTER TABLE `usermain`
  MODIFY `UserID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `userinventory`
--
ALTER TABLE `userinventory`
  ADD CONSTRAINT `userinventory_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `usermain` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
