---
layout: default
title: MajutsuCity: Language-driven Aesthetic-adaptive City Generation with Controllable 3D Assets and Layouts
---

# MajutsuCity: Language-driven Aesthetic-adaptive City Generation with Controllable 3D Assets and Layouts

**arXiv**: [2511.20415v1](https://arxiv.org/abs/2511.20415) | [PDF](https://arxiv.org/pdf/2511.20415.pdf)

**作者**: Zilong Huang, Jun He, Xiaobin Huang, Ziyi Xiong, Yang Luo, Junyan Ye, Weijia Li, Yiping Chen, Ting Han

---

## 💡 一句话要点

**提出MajutsuCity框架，通过语言驱动生成可控3D城市场景，解决风格多样性与结构一致性问题。**

**关键词**: `3D城市生成` `语言驱动控制` `美学自适应` `可控布局` `多模态数据集` `交互编辑`

## 📋 核心要点

1. 核心问题：现有方法难以平衡文本生成创意与显式结构编辑性。
2. 方法要点：采用四阶段流程，集成布局、资产和材料，并引入交互编辑代理。
3. 实验或效果：布局FID降低83.7%，在AQS和RDR指标上领先现有方法。

## 📄 摘要（原文）

> Generating realistic 3D cities is fundamental to world models, virtual reality, and game development, where an ideal urban scene must satisfy both stylistic diversity, fine-grained, and controllability. However, existing methods struggle to balance the creative flexibility offered by text-based generation with the object-level editability enabled by explicit structural representations. We introduce MajutsuCity, a natural language-driven and aesthetically adaptive framework for synthesizing structurally consistent and stylistically diverse 3D urban scenes. MajutsuCity represents a city as a composition of controllable layouts, assets, and materials, and operates through a four-stage pipeline. To extend controllability beyond initial generation, we further integrate MajutsuAgent, an interactive language-grounded editing agent} that supports five object-level operations. To support photorealistic and customizable scene synthesis, we also construct MajutsuDataset, a high-quality multimodal dataset} containing 2D semantic layouts and height maps, diverse 3D building assets, and curated PBR materials and skyboxes, each accompanied by detailed annotations. Meanwhile, we develop a practical set of evaluation metrics, covering key dimensions such as structural consistency, scene complexity, material fidelity, and lighting atmosphere. Extensive experiments demonstrate MajutsuCity reduces layout FID by 83.7% compared with CityDreamer and by 20.1% over CityCraft. Our method ranks first across all AQS and RDR scores, outperforming existing methods by a clear margin. These results confirm MajutsuCity as a new state-of-the-art in geometric fidelity, stylistic adaptability, and semantic controllability for 3D city generation. We expect our framework can inspire new avenues of research in 3D city generation. Our dataset and code will be released at https://github.com/LongHZ140516/MajutsuCity.

