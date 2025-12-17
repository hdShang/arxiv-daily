---
layout: default
title: Localising under the drape: proprioception in the era of distributed surgical robotic system
---

# Localising under the drape: proprioception in the era of distributed surgical robotic system

**arXiv**: [2510.23512v1](https://arxiv.org/abs/2510.23512) | [PDF](https://arxiv.org/pdf/2510.23512.pdf)

**作者**: Martin Huber, Nicola A. Cavalcanti, Ayoob Davoodi, Ruixuan Li, Christopher E. Mower, Fabio Carrillo, Christoph J. Laux, Francois Teyssere, Thibault Chandanson, Antoine Harlé, Elie Saghbiny, Mazda Farshad, Guillaume Morel, Emmanuel Vander Poorten, Philipp Fürnstahl, Sébastien Ourselin, Christos Bergeles, Tom Vercauteren

---

## 💡 一句话要点

**提出无标记本体感知方法，以解决分布式手术机器人定位问题。**

**关键词**: `手术机器人定位` `无标记感知` `立体视觉` `Transformer模型` `多机器人系统` `手术场景理解`

## 📋 核心要点

1. 核心问题：手术机器人缺乏空间感知，易碰撞且硬件负担重。
2. 方法要点：使用轻量立体RGB相机和Transformer模型，无需标记。
3. 实验或效果：基于大规模数据集，提升跟踪可见度25%，支持多机器人交互。

## 📄 摘要（原文）

> Despite their mechanical sophistication, surgical robots remain blind to
> their surroundings. This lack of spatial awareness causes collisions, system
> recoveries, and workflow disruptions, issues that will intensify with the
> introduction of distributed robots with independent interacting arms. Existing
> tracking systems rely on bulky infrared cameras and reflective markers,
> providing only limited views of the surgical scene and adding hardware burden
> in crowded operating rooms. We present a marker-free proprioception method that
> enables precise localisation of surgical robots under their sterile draping
> despite associated obstruction of visual cues. Our method solely relies on
> lightweight stereo-RGB cameras and novel transformer-based deep learning
> models. It builds on the largest multi-centre spatial robotic surgery dataset
> to date (1.4M self-annotated images from human cadaveric and preclinical in
> vivo studies). By tracking the entire robot and surgical scene, rather than
> individual markers, our approach provides a holistic view robust to occlusions,
> supporting surgical scene understanding and context-aware control. We
> demonstrate an example of potential clinical benefits during in vivo breathing
> compensation with access to tissue dynamics, unobservable under state of the
> art tracking, and accurately locate in multi-robot systems for future
> intelligent interaction. In addition, and compared with existing systems, our
> method eliminates markers and improves tracking visibility by 25%. To our
> knowledge, this is the first demonstration of marker-free proprioception for
> fully draped surgical robots, reducing setup complexity, enhancing safety, and
> paving the way toward modular and autonomous robotic surgery.

