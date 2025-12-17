---
layout: default
title: Language-guided 3D scene synthesis for fine-grained functionality understanding
---

# Language-guided 3D scene synthesis for fine-grained functionality understanding

**arXiv**: [2511.23230v1](https://arxiv.org/abs/2511.23230) | [PDF](https://arxiv.org/pdf/2511.23230.pdf)

**作者**: Jaime Corsetti, Francesco Giuliari, Davide Boscaini, Pedro Hermosilla, Andrea Pilzer, Guofeng Mei, Alexandros Delitzas, Francis Engelmann, Fabio Poiesi

---

## 💡 一句话要点

**提出SynthFun3D方法，通过语言引导合成3D场景以解决细粒度功能理解的数据稀缺问题。**

**关键词**: `3D场景合成` `功能理解` `语言引导` `数据生成` `细粒度标注`

## 📋 核心要点

1. 核心问题：3D功能理解因真实数据收集和标注成本高而受限，缺乏大规模标注数据。
2. 方法要点：基于动作描述，利用带部件级标注的家具数据库自动合成可完成动作的3D室内场景，并识别功能元素掩码。
3. 实验或效果：用户研究显示场景-提示一致性提升，生成数据可替代或补充真实数据，性能损失小或提升。

## 📄 摘要（原文）

> Functionality understanding in 3D, which aims to identify the functional element in a 3D scene to complete an action (e.g., the correct handle to "Open the second drawer of the cabinet near the bed"), is hindered by the scarcity of real-world data due to the substantial effort needed for its collection and annotation. To address this, we introduce SynthFun3D, the first method for task-based 3D scene synthesis. Given the action description, SynthFun3D generates a 3D indoor environment using a furniture asset database with part-level annotation, ensuring the action can be accomplished. It reasons about the action to automatically identify and retrieve the 3D mask of the correct functional element, enabling the inexpensive and large-scale generation of high-quality annotated data. We validate SynthFun3D through user studies, which demonstrate improved scene-prompt coherence compared to other approaches. Our quantitative results further show that the generated data can either replace real data with minor performance loss or supplement real data for improved performance, thereby providing an inexpensive and scalable solution for data-hungry 3D applications. Project page: github.com/tev-fbk/synthfun3d.

