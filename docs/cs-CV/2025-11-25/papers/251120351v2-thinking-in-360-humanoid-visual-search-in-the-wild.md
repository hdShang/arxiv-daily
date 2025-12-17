---
layout: default
title: Thinking in 360°: Humanoid Visual Search in the Wild
---

# Thinking in 360°: Humanoid Visual Search in the Wild

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.20351" class="toolbar-btn" target="_blank">📄 arXiv: 2511.20351v2</a>
  <a href="https://arxiv.org/pdf/2511.20351.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.20351v2" onclick="toggleFavorite(this, '2511.20351v2', 'Thinking in 360°: Humanoid Visual Search in the Wild')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Heyang Yu, Yinan Han, Xiangyu Zhang, Baiqiao Yin, Bowen Chang, Xiangyu Han, Xinhao Liu, Jing Zhang, Marco Pavone, Chen Feng, Saining Xie, Yiming Li

**分类**: cs.CV

**发布日期**: 2025-11-25 (更新: 2025-11-26)

**备注**: Website: https://humanoid-vstar.github.io/ ; Code: https://github.com/humanoid-vstar/hstar

---

## 💡 一句话要点

**提出H* Bench基准，研究具身智能体在360°全景图像中的视觉搜索能力。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `具身智能` `视觉搜索` `360°全景图像` `人型智能体` `多模态大语言模型`

## 📋 核心要点

1. 现有视觉搜索方法忽略了具身智能体与3D世界的交互，无法模拟人类在360°环境下的搜索行为。
2. 提出人型视觉搜索，让人型智能体主动旋转头部，在360°全景图像中搜索物体或路径，模拟人类视觉搜索。
3. 构建H* Bench基准，包含复杂的真实场景，实验表明优化后的Qwen2.5-VL模型在物体和路径搜索任务中性能显著提升。

## 📝 摘要（中文）

本文提出了一种人型视觉搜索方法，模拟人类通过头部和眼睛的协同控制在360°环境中进行视觉信息搜索。为了克服现有视觉搜索方法局限于静态图像的缺点，并摆脱现实世界硬件的限制，本文构建了一个名为H* Bench的新基准，该基准包含交通枢纽、大型零售空间、城市街道和公共机构等复杂的真实场景，用于评估智能体在视觉拥挤环境中的视觉空间推理能力。实验表明，即使是顶级的商业模型在物体和路径搜索任务中也仅能达到约30%的成功率。通过后训练技术优化开源的Qwen2.5-VL模型，物体搜索的成功率从14.83%提升至47.38%，路径搜索的成功率从6.44%提升至24.94%。路径搜索较低的上限表明其难度更高，这归因于对复杂空间常识的需求。研究结果展示了具身智能体的发展前景，同时也量化了构建能够无缝集成到日常人类生活中的多模态大语言模型智能体所面临的巨大挑战。

## 🔬 方法详解

**问题定义**：论文旨在解决现有视觉搜索方法无法模拟人类在360°全景环境中进行视觉搜索的问题。现有方法主要处理静态图像，忽略了头部运动和环境交互，限制了智能体在复杂场景中的应用。此外，缺乏针对真实世界复杂场景的基准数据集，阻碍了相关研究的进展。

**核心思路**：论文的核心思路是让人型智能体模拟人类的头部运动，通过主动旋转头部来探索360°全景图像，从而进行物体或路径搜索。这种方法模拟了人类视觉搜索的自然方式，能够更好地利用环境信息，提高搜索效率。

**技术框架**：整体框架包含以下几个主要部分：1）360°全景图像输入；2）人型智能体模型，负责控制头部旋转；3）视觉搜索模型，用于识别目标物体或路径；4）H* Bench基准数据集，用于评估智能体的性能。智能体通过不断调整头部姿态，观察全景图像，并利用视觉搜索模型判断目标是否存在或路径是否可行。

**关键创新**：论文的关键创新在于提出了人型视觉搜索的概念，并将具身智能体引入到360°全景图像搜索中。此外，构建了H* Bench基准数据集，该数据集包含复杂的真实世界场景，更具挑战性。通过后训练技术优化开源的Qwen2.5-VL模型，使其在H* Bench基准上取得了显著的性能提升。

**关键设计**：论文使用Qwen2.5-VL作为视觉搜索模型，并通过后训练技术对其进行优化。后训练的具体细节未知，但目标是提高模型在H* Bench基准上的物体和路径搜索能力。损失函数和网络结构等细节未在摘要中详细说明。

## 📊 实验亮点

实验结果表明，即使是顶级的商业模型在H* Bench基准上的物体和路径搜索任务中也仅能达到约30%的成功率。通过后训练技术优化开源的Qwen2.5-VL模型，物体搜索的成功率从14.83%提升至47.38%，路径搜索的成功率从6.44%提升至24.94%。这表明，通过适当的模型优化和训练，多模态大语言模型在具身视觉搜索任务中具有很大的潜力。

## 🎯 应用场景

该研究成果可应用于机器人导航、虚拟现实、增强现实等领域。例如，可以开发智能导盲机器人，帮助视障人士在复杂环境中安全导航；也可以应用于虚拟旅游，让用户通过控制虚拟人型智能体探索360°全景场景。此外，该研究对于提升多模态大语言模型在具身智能体中的应用具有重要意义。

## 📄 摘要（原文）

> Humans rely on the synergistic control of head (cephalomotor) and eye (oculomotor) to efficiently search for visual information in 360°. However, prior approaches to visual search are limited to a static image, neglecting the physical embodiment and its interaction with the 3D world. How can we develop embodied visual search agents as efficient as humans while bypassing the constraints imposed by real-world hardware? To this end, we propose humanoid visual search where a humanoid agent actively rotates its head to search for objects or paths in an immersive world represented by a 360° panoramic image. To study visual search in visually-crowded real-world scenarios, we build H* Bench, a new benchmark that moves beyond household scenes to challenging in-the-wild scenes that necessitate advanced visual-spatial reasoning capabilities, such as transportation hubs, large-scale retail spaces, urban streets, and public institutions. Our experiments first reveal that even top-tier proprietary models falter, achieving only ~30% success in object and path search. We then use post-training techniques to enhance the open-source Qwen2.5-VL, increasing its success rate by over threefold for both object search (14.83% to 47.38%) and path search (6.44% to 24.94%). Notably, the lower ceiling of path search reveals its inherent difficulty, which we attribute to the demand for sophisticated spatial commonsense. Our results not only show a promising path forward but also quantify the immense challenge that remains in building MLLM agents that can be seamlessly integrated into everyday human life.

