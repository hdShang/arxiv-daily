---
layout: default
title: Self-supervised perception for tactile skin covered dexterous hands
---

# Self-supervised perception for tactile skin covered dexterous hands

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11420" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11420v1</a>
  <a href="https://arxiv.org/pdf/2505.11420.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11420v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11420v1', 'Self-supervised perception for tactile skin covered dexterous hands')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Akash Sharma, Carolina Higuera, Chaithanya Krishna Bodduluri, Zixi Liu, Taosha Fan, Tess Hellebrekers, Mike Lambeta, Byron Boots, Michael Kaess, Tingfan Wu, Francois Robert Hogan, Mustafa Mukadam

**分类**: cs.RO

**发布日期**: 2025-05-16

**备注**: 18 pages, 15 figures

---

## 💡 一句话要点

**提出Sparsh-skin以解决机器人手部触觉感知问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `触觉感知` `自我监督学习` `机器人手` `磁性传感器` `潜在嵌入` `灵巧机器人` `数据蒸馏`

## 📋 核心要点

1. 现有的触觉传感器多集中于手指尖，缺乏全手覆盖的通用模型，限制了机器人的灵巧性。
2. 论文提出Sparsh-skin，通过自我蒸馏技术，利用未标记的手-物体交互数据生成潜在触觉嵌入。
3. 实验结果显示，Sparsh-skin在多个基准任务中提升了41%以上的性能，相比于端到端学习提升超过56%。

## 📝 摘要（中文）

我们提出了Sparsh-skin，这是一个针对分布在灵巧机器人手指尖、指骨和手掌的磁性皮肤传感器的预训练编码器。与受限于指尖且带宽有限的视觉触觉传感器相比，磁性触觉皮肤提供了灵活的形态和快速的响应时间。完整的手部触觉感知对机器人灵巧性至关重要。然而，缺乏通用模型以及对磁通量的解释和校准的挑战限制了这些传感器的采用。Sparsh-skin通过对一系列未标记的手-物体交互进行自我蒸馏，自我监督地输出潜在的触觉嵌入，可用于任何下游任务。在多个基准任务的实验中，我们发现预训练的Sparsh-skin表示在学习下游任务时样本效率高，并且相比于之前的工作提高了超过41%的任务性能，相比于端到端学习提高了超过56%。

## 🔬 方法详解

**问题定义**：本论文旨在解决灵巧机器人手部触觉感知的不足，现有方法主要集中在手指尖，缺乏全手覆盖的能力，且对磁性触觉传感器的解释和校准存在挑战。

**核心思路**：Sparsh-skin通过自我监督学习，利用未标记的手-物体交互数据进行自我蒸馏，生成潜在的触觉嵌入，从而提升触觉感知的有效性和适用性。

**技术框架**：整体架构包括数据采集、特征提取和潜在嵌入生成三个主要模块。首先，使用Xela uSkin传感器收集手部的运动和触觉数据；然后，通过编码器提取特征；最后，生成可用于下游任务的潜在嵌入。

**关键创新**：最重要的技术创新在于自我蒸馏的使用，使得模型能够在没有标记数据的情况下进行有效学习，克服了传统方法对标记数据的依赖。

**关键设计**：在模型设计中，采用了特定的损失函数以优化潜在嵌入的质量，并通过多层神经网络结构增强特征提取能力，确保了模型在不同任务中的适应性和性能。

## 📊 实验亮点

实验结果表明，预训练的Sparsh-skin在多个基准任务中表现优异，任务性能提升超过41%，相比于端到端学习提升超过56%，显示出其在样本效率和任务适应性方面的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括机器人抓取、物体操作和人机交互等场景。通过提升机器人手部的触觉感知能力，Sparsh-skin能够使机器人在复杂环境中更灵活地执行任务，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We present Sparsh-skin, a pre-trained encoder for magnetic skin sensors distributed across the fingertips, phalanges, and palm of a dexterous robot hand. Magnetic tactile skins offer a flexible form factor for hand-wide coverage with fast response times, in contrast to vision-based tactile sensors that are restricted to the fingertips and limited by bandwidth. Full hand tactile perception is crucial for robot dexterity. However, a lack of general-purpose models, challenges with interpreting magnetic flux and calibration have limited the adoption of these sensors. Sparsh-skin, given a history of kinematic and tactile sensing across a hand, outputs a latent tactile embedding that can be used in any downstream task. The encoder is self-supervised via self-distillation on a variety of unlabeled hand-object interactions using an Allegro hand sensorized with Xela uSkin. In experiments across several benchmark tasks, from state estimation to policy learning, we find that pretrained Sparsh-skin representations are both sample efficient in learning downstream tasks and improve task performance by over 41% compared to prior work and over 56% compared to end-to-end learning.

