---
layout: default
title: "V2V-GoT: Vehicle-to-Vehicle Cooperative Autonomous Driving with Multimodal Large Language Models and Graph-of-Thoughts"
---

# V2V-GoT: Vehicle-to-Vehicle Cooperative Autonomous Driving with Multimodal Large Language Models and Graph-of-Thoughts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18053" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18053v3</a>
  <a href="https://arxiv.org/pdf/2509.18053.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18053v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18053v3', 'V2V-GoT: Vehicle-to-Vehicle Cooperative Autonomous Driving with Multimodal Large Language Models and Graph-of-Thoughts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hsu-kuang Chiu, Ryo Hachiuma, Chien-Yi Wang, Yu-Chiang Frank Wang, Min-Hung Chen, Stephen F. Smith

**分类**: cs.RO

**发布日期**: 2025-09-22 (更新: 2025-09-25)

**备注**: Our project website: https://eddyhkchiu.github.io/v2vgot.github.io/

**🔗 代码/项目**: [PROJECT_PAGE](https://eddyhkchiu.github.io/v2vgot.github.io/)

---

## 💡 一句话要点

**提出V2V-GoT，利用多模态大语言模型和图推理解决V2V协同自动驾驶中的遮挡问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `V2V协同驾驶` `多模态大语言模型` `图推理` `遮挡感知` `自动驾驶` `协同感知` `车辆互联`

## 📋 核心要点

1. 现有自动驾驶车辆在传感器被遮挡时存在安全隐患，V2V协同驾驶是潜在解决方案。
2. 论文提出V2V-GoT框架，利用多模态大语言模型和图推理进行协同感知和规划。
3. 实验结果表明，V2V-GoT在协同感知、预测和规划任务中优于现有方法。

## 📝 摘要（中文）

当前最先进的自动驾驶车辆在道路上被大型物体遮挡局部传感器时，可能会面临安全 критических ситуациях。车辆到车辆（V2V）协同自动驾驶被提出作为解决此问题的一种手段。最近引入的一种协同自动驾驶框架进一步采用了一种结合多模态大语言模型（MLLM）的方法，以整合协同感知和规划过程。然而，尽管将图推理应用于MLLM具有潜在的好处，但之前的协同自动驾驶研究并未考虑这一想法。在本文中，我们提出了一种专门为基于MLLM的协同自动驾驶设计的新的图推理框架。我们的图推理包括我们提出的遮挡感知感知和规划感知预测的新颖想法。我们整理了V2V-GoT-QA数据集，并开发了V2V-GoT模型，用于训练和测试协同驾驶图推理。我们的实验结果表明，我们的方法在协同感知、预测和规划任务中优于其他基线。

## 🔬 方法详解

**问题定义**：论文旨在解决V2V协同自动驾驶中，由于车辆传感器被遮挡而导致的安全问题。现有方法虽然利用MLLM进行协同感知和规划，但缺乏有效的推理机制，无法充分利用多车辆的信息，尤其是在存在遮挡的情况下。

**核心思路**：论文的核心思路是引入图推理（Graph-of-Thoughts, GoT）机制，结合MLLM，构建一个更强大的协同自动驾驶系统。通过GoT，系统可以进行更深入的推理和决策，从而更好地处理遮挡等复杂情况。这种设计旨在模拟人类驾驶员在协同驾驶中的思考过程，即综合考虑多个车辆的感知信息，并进行推理和预测。

**技术框架**：V2V-GoT框架包含以下主要模块：1) 多模态输入：接收来自多个车辆的感知数据，包括图像、激光雷达等；2) MLLM编码器：利用MLLM对多模态数据进行编码，提取特征；3) 图构建：基于车辆之间的关系（例如距离、相对位置）构建图结构；4) 图推理：在图上进行推理，例如遮挡感知感知和规划感知预测；5) 决策输出：根据推理结果，生成协同驾驶决策，例如加速、减速、变道等。

**关键创新**：论文的关键创新在于将图推理（GoT）引入到MLLM-based的V2V协同自动驾驶中。具体而言，提出了遮挡感知感知和规划感知预测两种新的图推理策略。遮挡感知感知旨在利用其他车辆的视角来弥补自身车辆的感知盲区。规划感知预测则考虑了其他车辆的规划意图，从而更准确地预测其未来行为。

**关键设计**：论文提出了V2V-GoT-QA数据集，用于训练和测试协同驾驶图推理。具体的技术细节（例如MLLM的具体选择、图推理算法、损失函数等）在论文中可能有所描述，但摘要中未明确提及。这些细节对于复现和进一步研究至关重要，需要查阅原文。

## 📊 实验亮点

实验结果表明，V2V-GoT在协同感知、预测和规划任务中均优于其他基线方法。具体性能提升数据未在摘要中给出，需要在论文中查找。V2V-GoT-QA数据集的构建也为相关研究提供了宝贵资源。

## 🎯 应用场景

该研究成果可应用于提高自动驾驶车辆在复杂交通环境下的安全性，尤其是在城市道路、交叉路口等容易发生遮挡的场景。通过车辆间的协同感知和推理，可以有效减少事故风险，提升交通效率。未来，该技术有望推广到车路协同系统，实现更高级别的自动驾驶。

## 📄 摘要（原文）

> Current state-of-the-art autonomous vehicles could face safety-critical situations when their local sensors are occluded by large nearby objects on the road. Vehicle-to-vehicle (V2V) cooperative autonomous driving has been proposed as a means of addressing this problem, and one recently introduced framework for cooperative autonomous driving has further adopted an approach that incorporates a Multimodal Large Language Model (MLLM) to integrate cooperative perception and planning processes. However, despite the potential benefit of applying graph-of-thoughts reasoning to the MLLM, this idea has not been considered by previous cooperative autonomous driving research. In this paper, we propose a novel graph-of-thoughts framework specifically designed for MLLM-based cooperative autonomous driving. Our graph-of-thoughts includes our proposed novel ideas of occlusion-aware perception and planning-aware prediction. We curate the V2V-GoT-QA dataset and develop the V2V-GoT model for training and testing the cooperative driving graph-of-thoughts. Our experimental results show that our method outperforms other baselines in cooperative perception, prediction, and planning tasks. Our project website: https://eddyhkchiu.github.io/v2vgot.github.io/ .

