library(ggplot2)
library(palmerpenguins)
library(tidyverse)
penguins %>%
  drop_na(sex) %>%
  ggplot(aes(x=flipper_length_mm, y=body_mass_g)) +
  geom_point(aes(color=species, shape=species)) +
  facet_wrap(~sex)
#glimpse(penguins)

ggplot(data=penguins, aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point(color="purple")

ggplot(data=penguins, aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point(color="purple")

ggplot(data=penguins, aes(x = flipper_length_mm, y = body_mass_g)) +
  geom_point(aes(color=species, shape=species)) +labs(title = "Three Penguins")+
  facet_wrap(~sex)

