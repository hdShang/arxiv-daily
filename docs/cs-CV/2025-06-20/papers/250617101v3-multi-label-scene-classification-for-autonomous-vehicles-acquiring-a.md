---
layout: default
title: "Multi-label Scene Classification for Autonomous Vehicles: Acquiring and Accumulating Knowledge from Diverse Datasets"
---

# Multi-label Scene Classification for Autonomous Vehicles: Acquiring and Accumulating Knowledge from Diverse Datasets

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17101" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17101v3</a>
  <a href="https://arxiv.org/pdf/2506.17101.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17101v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17101v3', 'Multi-label Scene Classification for Autonomous Vehicles: Acquiring and Accumulating Knowledge from Diverse Datasets')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ke Li, Chenyu Zhang, Yuxin Ding, Xianbiao Hu, Ruwen Qin

**分类**: cs.CV

**发布日期**: 2025-06-20 (更新: 2025-09-17)

**🔗 代码/项目**: [GITHUB](https://github.com/KELISBU/KAA-CAL)

---

## 💡 一句话要点

**提出KAA-CAL以解决自动驾驶场景多标签分类问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `多标签分类` `知识获取` `主动学习` `深度学习` `场景识别` `数据集`

## 📋 核心要点

1. 现有方法在多标签场景分类中面临数据集获取困难和新属性出现时需重新注释的挑战。
2. 论文提出的KAA-CAL方法通过知识获取与积累和主动学习相结合，解决了多标签分类的适应性问题。
3. 实验结果显示，KAA-CAL在DSI数据集上提升了56.1%，并在其他数据集上以更少的数据实现了更好的性能。

## 📝 摘要（中文）

驾驶场景本质上是异质和动态的。多属性场景识别作为一种高级视觉感知能力，为自动驾驶车辆提供了必要的上下文意识，以理解、推理和与复杂驾驶环境互动。尽管场景识别最好通过多任务学习建模为多标签分类问题，但面临两个主要挑战：获取平衡且全面注释的数据集的困难，以及当新属性出现时需要重新注释所有训练数据。为了解决这些挑战，本文提出了一种新颖的深度学习方法，将知识获取与积累（KAA）与基于一致性的主动学习（CAL）相结合。KAA利用异质单标签数据集的单任务学习建立知识基础，而CAL则弥合单标签和多标签数据之间的差距，适应多标签场景分类的基础模型。对新开发的驾驶场景识别（DSI）数据集的消融研究表明，相较于ImageNet预训练基线，提升了56.1%。此外，KAA-CAL在BDD100K和HSD数据集上超越了最先进的多标签分类方法，使用的数据量减少了85%，甚至能够识别在基础模型训练期间未见过的属性。

## 🔬 方法详解

**问题定义**：本文旨在解决自动驾驶场景的多标签分类问题，现有方法在获取平衡数据集和应对新属性时存在显著不足。

**核心思路**：通过结合知识获取与积累（KAA）和基于一致性的主动学习（CAL），构建一个适应性强的多标签分类框架，以便有效利用异质数据。

**技术框架**：整体架构包括两个主要模块：KAA模块用于从单标签数据集中获取知识，CAL模块则用于将这些知识适应到多标签场景分类中。

**关键创新**：最重要的技术创新在于KAA-CAL方法的提出，它通过有效整合单标签和多标签学习，显著提高了分类性能，并减少了对数据的需求。

**关键设计**：在模型设计中，采用了特定的损失函数以平衡不同标签的影响，同时在网络结构上进行了优化，以适应多标签的特性。具体参数设置和网络细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果显示，KAA-CAL方法在新开发的DSI数据集上相较于ImageNet预训练基线提升了56.1%。此外，该方法在BDD100K和HSD数据集上超越了现有的多标签分类技术，且使用的数据量减少了85%，展现出强大的数据效率和适应性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶系统、智能交通管理和城市环境监测等。通过提升自动驾驶车辆对复杂场景的理解能力，能够显著提高行车安全性和效率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Driving scenes are inherently heterogeneous and dynamic. Multi-attribute scene identification, as a high-level visual perception capability, provides autonomous vehicles (AVs) with essential contextual awareness to understand, reason through, and interact with complex driving environments. Although scene identification is best modeled as a multi-label classification problem via multitask learning, it faces two major challenges: the difficulty of acquiring balanced, comprehensively annotated datasets and the need to re-annotate all training data when new attributes emerge. To address these challenges, this paper introduces a novel deep learning method that integrates Knowledge Acquisition and Accumulation (KAA) with Consistency-based Active Learning (CAL). KAA leverages monotask learning on heterogeneous single-label datasets to build a knowledge foundation, while CAL bridges the gap between single- and multi-label data, adapting the foundation model for multi-label scene classification. An ablation study on the newly developed Driving Scene Identification (DSI) dataset demonstrates a 56.1% improvement over an ImageNet-pretrained baseline. Moreover, KAA-CAL outperforms state-of-the-art multi-label classification methods on the BDD100K and HSD datasets, achieving this with 85% less data and even recognizing attributes unseen during foundation model training. The DSI dataset and KAA-CAL implementation code are publicly available at https://github.com/KELISBU/KAA-CAL .

