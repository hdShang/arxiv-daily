---
layout: default
title: Thinking in 360°: Humanoid Visual Search in the Wild
---

# Thinking in 360°: Humanoid Visual Search in the Wild

**arXiv**: [2511.20351v1](https://arxiv.org/abs/2511.20351) | [PDF](https://arxiv.org/pdf/2511.20351.pdf)

**作者**: Heyang Yu, Yinan Han, Xiangyu Zhang, Baiqiao Yin, Bowen Chang, Xiangyu Han, Xinhao Liu, Jing Zhang, Marco Pavone, Chen Feng, Saining Xie, Yiming Li

---

## 💡 一句话要点

**提出人形视觉搜索方法以在360°全景中高效搜索物体和路径**

**关键词**: `人形视觉搜索` `360°全景图像` `视觉空间推理` `后训练技术` `基准数据集`

## 📋 核心要点

1. 核心问题：现有视觉搜索方法局限于静态图像，忽略物理交互和3D世界。
2. 方法要点：构建人形代理主动旋转头部，在H* Bench基准中模拟真实场景。
3. 实验或效果：通过后训练提升Qwen2.5-VL，物体搜索成功率从14.83%增至47.38%。

## 📄 摘要（原文）

> Humans rely on the synergistic control of head (cephalomotor) and eye (oculomotor) to efficiently search for visual information in 360°. However, prior approaches to visual search are limited to a static image, neglecting the physical embodiment and its interaction with the 3D world. How can we develop embodied visual search agents as efficient as humans while bypassing the constraints imposed by real-world hardware? To this end, we propose humanoid visual search where a humanoid agent actively rotates its head to search for objects or paths in an immersive world represented by a 360° panoramic image. To study visual search in visually-crowded real-world scenarios, we build H* Bench, a new benchmark that moves beyond household scenes to challenging in-the-wild scenes that necessitate advanced visual-spatial reasoning capabilities, such as transportation hubs, large-scale retail spaces, urban streets, and public institutions. Our experiments first reveal that even top-tier proprietary models falter, achieving only ~30% success in object and path search. We then use post-training techniques to enhance the open-source Qwen2.5-VL, increasing its success rate by over threefold for both object search (14.83% to 47.38%) and path search (6.44% to 24.94%). Notably, the lower ceiling of path search reveals its inherent difficulty, which we attribute to the demand for sophisticated spatial commonsense. Our results not only show a promising path forward but also quantify the immense challenge that remains in building MLLM agents that can be seamlessly integrated into everyday human life.

