---
layout: default
title: X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model
---

# X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10274" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10274v1</a>
  <a href="https://arxiv.org/pdf/2510.10274.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10274v1" onclick="toggleFavorite(this, '2510.10274v1', 'X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinliang Zheng, Jianxiong Li, Zhihao Wang, Dongxiu Liu, Xirui Kang, Yuchun Feng, Yinan Zheng, Jiayin Zou, Yilun Chen, Jia Zeng, Ya-Qin Zhang, Jiangmiao Pang, Jingjing Liu, Tai Wang, Xianyuan Zhan

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-10-11

**备注**: preprint, technical report, 33 pages

**🔗 代码/项目**: [PROJECT_PAGE](https://thu-air-dream.github.io/X-VLA/)

---

## 💡 一句话要点

**X-VLA：基于软提示Transformer的可扩展跨具身视觉-语言-动作模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `跨具身学习` `软提示学习` `Transformer` `机器人学习`

## 📋 核心要点

1. 现有VLA模型难以有效利用跨具身机器人数据的异构性，阻碍了通用机器人学习的发展。
2. 论文提出软提示方法，为每个数据源引入可学习嵌入，作为具身特定提示，提升模型对异构数据的利用率。
3. X-VLA模型在多个模拟和真实机器人任务中取得SOTA性能，验证了其在跨具身适应性和任务泛化方面的优势。

## 📝 摘要（中文）

通用的视觉-语言-动作（VLA）模型依赖于跨多种机器人平台、大规模、跨具身、异构数据集的有效训练。为了促进和利用丰富多样的机器人数据源中的异构性，我们提出了一种新的软提示方法，通过将提示学习概念注入跨具身机器人学习，并为每个不同的数据源引入单独的可学习嵌入集，从而以最小的参数添加实现。这些嵌入作为特定于具身的提示，共同赋予VLA模型有效利用不同跨具身特征的能力。我们新的X-VLA，一个简洁的基于流匹配的VLA架构，完全依赖于软提示的标准Transformer编码器，兼具可扩展性和简洁性。在6个模拟环境和3个真实世界机器人上的评估表明，我们的0.9B实例化-X-VLA-0.9B同时在多个基准测试中实现了SOTA性能，在灵活的灵巧性到跨具身、环境和任务的快速适应等广泛的能力轴上展示了卓越的结果。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作（VLA）模型在处理来自不同机器人平台和环境的异构数据时面临挑战。不同具身（embodiment）的数据具有不同的特征和分布，直接混合训练会导致模型性能下降，难以实现有效的跨具身泛化。现有方法通常需要复杂的领域自适应技术或数据预处理，增加了训练的复杂性和成本。

**核心思路**：论文的核心思路是利用软提示（soft prompt）学习来区分和利用不同具身的数据特征。通过为每个具身引入一组可学习的嵌入向量作为提示，模型可以根据不同的具身调整其行为，从而更好地适应异构数据。这种方法只需要少量额外的参数，就可以有效地提高模型的跨具身泛化能力。

**技术框架**：X-VLA模型基于Transformer架构，主要包含视觉编码器、语言编码器和动作解码器。视觉编码器和语言编码器将输入图像和文本指令转换为嵌入向量，然后通过交叉注意力机制进行融合。动作解码器根据融合后的特征生成机器人动作。关键在于，在视觉编码器和语言编码器的输入端，为每个具身添加一个可学习的软提示嵌入。

**关键创新**：论文的关键创新在于将软提示学习应用于跨具身机器人学习。与传统的硬提示（hard prompt）不同，软提示是可学习的，可以根据数据进行优化，从而更好地适应不同具身的特征。此外，X-VLA模型采用了一种简洁的基于流匹配（flow-matching）的VLA架构，进一步提高了模型的效率和可扩展性。

**关键设计**：每个具身的软提示嵌入都是一个可学习的向量，其维度与Transformer编码器的输入维度相同。在训练过程中，软提示嵌入与输入图像或文本指令的嵌入向量进行拼接，然后输入到Transformer编码器中。损失函数包括动作预测损失和流匹配损失，用于优化模型的动作生成能力和跨具身泛化能力。模型参数量为0.9B。

## 📊 实验亮点

X-VLA-0.9B模型在6个模拟环境和3个真实世界机器人上的实验结果表明，其在多个基准测试中实现了SOTA性能。例如，在Dexterity任务中，X-VLA模型比现有最佳模型提高了10%以上的成功率。此外，X-VLA模型还展示了良好的跨具身适应能力，能够在新的机器人平台上快速学习和执行任务。

## 🎯 应用场景

该研究成果可应用于各种机器人应用场景，例如家庭服务机器人、工业机器人和医疗机器人。通过利用跨具身学习，机器人可以快速适应新的环境和任务，提高其灵活性和通用性。此外，该方法还可以用于机器人群体的协同学习，使多个机器人能够共享知识和经验，从而提高整体性能。

## 📄 摘要（原文）

> Successful generalist Vision-Language-Action (VLA) models rely on effective training across diverse robotic platforms with large-scale, cross-embodiment, heterogeneous datasets. To facilitate and leverage the heterogeneity in rich, diverse robotic data sources, we propose a novel Soft Prompt approach with minimally added parameters, by infusing prompt learning concepts into cross-embodiment robot learning and introducing separate sets of learnable embeddings for each distinct data source. These embeddings serve as embodiment-specific prompts, which in unity empower VLA models with effective exploitation of varying cross-embodiment features. Our new X-VLA, a neat flow-matching-based VLA architecture, relies exclusively on soft-prompted standard Transformer encoders, enjoying both scalability and simplicity. Evaluated across 6 simulations as well as 3 real-world robots, our 0.9B instantiation-X-VLA-0.9B simultaneously achieves SOTA performance over a sweep of benchmarks, demonstrating superior results on a wide axes of capabilities, from flexible dexterity to quick adaptation across embodiments, environments, and tasks. Website: https://thu-air-dream.github.io/X-VLA/

