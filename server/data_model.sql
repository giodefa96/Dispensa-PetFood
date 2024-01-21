CREATE TABLE `Agend` (
  `id` integer PRIMARY KEY,
  `user_id` integer,
  `pet_id` integer
);

CREATE TABLE `Appointment` (
  `id` integer PRIMARY KEY,
  `agend_id` integer,
  `date` date,
  `description` varchar(255)
);

CREATE TABLE `User` (
  `id` integer PRIMARY KEY,
  `username` varchar(255),
  `name` varchar(255),
  `birthday` data,
  `description` longchar,
  `city` varchar(255),
  `address` varchar(255)
);

CREATE TABLE `Pet` (
  `id` integer PRIMARY KEY,
  `user_id` integer,
  `name` varchar(255),
  `vreed` varchar(255),
  `veterinarian_id` integer
);

CREATE TABLE `HistoricalAnimalCondition` (
  `id` integer PRIMARY KEY,
  `pet_id` integer,
  `weight` varchar(255),
  `age` varchar(255),
  `date` data
);

CREATE TABLE `Veterinarian` (
  `id` integer PRIMARY KEY,
  `clinic_id` integer,
  `name` varchar(255),
  `contact_number` phone_number,
  `email` email
);

CREATE TABLE `Vaccinations` (
  `id` integer PRIMARY KEY,
  `pet_id` integer,
  `date_somministration` date,
  `reactions` varchar(255)
);

CREATE TABLE `Clinic` (
  `id` integer PRIMARY KEY,
  `name` varchar(255),
  `address` varchar(255),
  `contact_number` varchar(255)
);

CREATE TABLE `OpeningHours` (
  `id` integer PRIMARY KEY,
  `clinic_id` integer,
  `day_of_the_week` varchar(255),
  `open_time` varchar(255),
  `close_time` varchar(255)
);

CREATE TABLE `Diet` (
  `id` integer PRIMARY KEY,
  `pet_id` integer,
  `start_date` date,
  `end_date` date
);

CREATE TABLE `Meal` (
  `id` integer PRIMARY KEY,
  `diet_id` integer,
  `product_id` integer,
  `feeding_time` timestamp
);

CREATE TABLE `PetProduct` (
  `id` integer PRIMARY KEY,
  `product_name` varchar(255),
  `price` varchar(255),
  `description` varchar(255)
);

CREATE TABLE `Medicine` (
  `id` integer PRIMARY KEY,
  `name` varchar(255)
);

CREATE TABLE `Stock` (
  `id` integer PRIMARY KEY,
  `product_id` integer,
  `quantity` varchar(255)
);

CREATE TABLE `Prescription` (
  `id` integer PRIMARY KEY,
  `pet_id` integer,
  `medicine_id` integer,
  `quantity` varchar(255),
  `date_start` date,
  `date_end` date
);

ALTER TABLE `User` ADD FOREIGN KEY (`id`) REFERENCES `Agend` (`user_id`);

ALTER TABLE `Agend` ADD FOREIGN KEY (`pet_id`) REFERENCES `Pet` (`id`);

ALTER TABLE `Appointment` ADD FOREIGN KEY (`agend_id`) REFERENCES `Agend` (`id`);

ALTER TABLE `Pet` ADD FOREIGN KEY (`user_id`) REFERENCES `User` (`id`);

CREATE TABLE `Pet_Veterinarian` (
  `Pet_veterinarian_id` integer,
  `Veterinarian_id` integer,
  PRIMARY KEY (`Pet_veterinarian_id`, `Veterinarian_id`)
);

ALTER TABLE `Pet_Veterinarian` ADD FOREIGN KEY (`Pet_veterinarian_id`) REFERENCES `Pet` (`veterinarian_id`);

ALTER TABLE `Pet_Veterinarian` ADD FOREIGN KEY (`Veterinarian_id`) REFERENCES `Veterinarian` (`id`);


ALTER TABLE `HistoricalAnimalCondition` ADD FOREIGN KEY (`pet_id`) REFERENCES `Pet` (`id`);

CREATE TABLE `Veterinarian_Clinic` (
  `Veterinarian_clinic_id` integer,
  `Clinic_id` integer,
  PRIMARY KEY (`Veterinarian_clinic_id`, `Clinic_id`)
);

ALTER TABLE `Veterinarian_Clinic` ADD FOREIGN KEY (`Veterinarian_clinic_id`) REFERENCES `Veterinarian` (`clinic_id`);

ALTER TABLE `Veterinarian_Clinic` ADD FOREIGN KEY (`Clinic_id`) REFERENCES `Clinic` (`id`);


ALTER TABLE `Vaccinations` ADD FOREIGN KEY (`pet_id`) REFERENCES `Pet` (`id`);

ALTER TABLE `OpeningHours` ADD FOREIGN KEY (`clinic_id`) REFERENCES `Clinic` (`id`);

ALTER TABLE `Diet` ADD FOREIGN KEY (`pet_id`) REFERENCES `Pet` (`id`);

ALTER TABLE `Meal` ADD FOREIGN KEY (`diet_id`) REFERENCES `Diet` (`id`);

ALTER TABLE `Meal` ADD FOREIGN KEY (`product_id`) REFERENCES `PetProduct` (`id`);

ALTER TABLE `PetProduct` ADD FOREIGN KEY (`id`) REFERENCES `Stock` (`product_id`);

ALTER TABLE `Medicine` ADD FOREIGN KEY (`id`) REFERENCES `Stock` (`product_id`);

ALTER TABLE `Prescription` ADD FOREIGN KEY (`pet_id`) REFERENCES `Pet` (`id`);

ALTER TABLE `Prescription` ADD FOREIGN KEY (`medicine_id`) REFERENCES `Medicine` (`id`);

ALTER TABLE `OpeningHours` ADD FOREIGN KEY (`close_time`) REFERENCES `OpeningHours` (`clinic_id`);
