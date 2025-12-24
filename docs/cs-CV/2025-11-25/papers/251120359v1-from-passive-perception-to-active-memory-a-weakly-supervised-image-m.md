---
layout: default
title: "From Passive Perception to Active Memory: A Weakly Supervised Image Manipulation Localization Framework Driven by Coarse-Grained Annotations"
---

# From Passive Perception to Active Memory: A Weakly Supervised Image Manipulation Localization Framework Driven by Coarse-Grained Annotations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.20359" class="toolbar-btn" target="_blank">📄 arXiv: 2511.20359v1</a>
  <a href="https://arxiv.org/pdf/2511.20359.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.20359v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.20359v1', 'From Passive Perception to Active Memory: A Weakly Supervised Image Manipulation Localization Framework Driven by Coarse-Grained Annotations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiqing Guo, Dongdong Xi, Songlin Li, Gaobo Yang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-25

**备注**: Accepted by AAAI 2026

---

## 💡 一句话要点

**提出BoxPromptIML框架，以低成本粗略标注实现图像篡改精确定位。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `图像篡改定位` `弱监督学习` `知识蒸馏` `粗略标注` `Segment Anything Model`

## 📋 核心要点

1. 现有图像篡改定位方法在标注成本和定位精度之间存在权衡，全监督方法成本高，弱监督方法精度低。
2. BoxPromptIML框架采用粗略区域标注策略，降低标注成本，并利用知识蒸馏训练轻量级学生模型。
3. 该方法在多个数据集上表现优异，在保持泛化能力的同时，实现了低成本和高效部署。

## 📝 摘要（中文）

图像篡改定位(IML)面临着最小化标注成本和实现精细定位精度之间的根本权衡。现有的全监督IML方法严重依赖于密集的像素级掩码标注，这限制了其向大型数据集或实际部署的可扩展性。相比之下，大多数现有的弱监督IML方法都基于图像级标签，这大大减少了标注工作，但通常缺乏精确的空间定位。为了解决这个难题，我们提出了一种新颖的弱监督IML框架BoxPromptIML，该框架有效地平衡了标注成本和定位性能。具体来说，我们提出了一种粗略区域标注策略，该策略可以以较低的成本生成相对准确的篡改掩码。为了提高模型效率并促进部署，我们进一步设计了一个高效的轻量级学生模型，该模型通过从基于Segment Anything Model (SAM)的固定教师模型中进行知识蒸馏来学习执行精细定位。此外，受到人类潜意识记忆机制的启发，我们的特征融合模块采用了一种双重引导策略，该策略利用从输入中获得的实时观察线索来主动地将回忆的原型模式进行情境化。这种策略不是被动特征提取，而是实现了一个动态的知识回忆过程，其中长期记忆适应当前图像的特定上下文，从而显著提高定位精度和鲁棒性。在分布内和分布外数据集上的大量实验表明，BoxPromptIML优于或可与全监督模型相媲美，同时保持了强大的泛化能力、低标注成本和高效的部署特性。

## 🔬 方法详解

**问题定义**：图像篡改定位旨在识别并定位图像中被篡改的区域。现有全监督方法需要像素级别的精确标注，成本高昂，难以扩展到大规模数据集。而弱监督方法虽然降低了标注成本，但定位精度往往不足，无法满足实际应用需求。因此，如何在降低标注成本的同时，保证定位精度，是图像篡改定位领域面临的关键问题。

**核心思路**：BoxPromptIML的核心思路是利用粗略的区域标注信息，结合知识蒸馏和记忆机制，实现高精度的图像篡改定位。通过粗略标注降低标注成本，利用预训练的SAM模型作为教师模型提供先验知识，并通过知识蒸馏将知识迁移到轻量级的学生模型，提高模型效率。同时，引入双重引导的特征融合模块，模拟人类的记忆机制，增强模型的定位能力。

**技术框架**：BoxPromptIML框架主要包含以下几个模块：1) 粗略区域标注模块：用于生成图像篡改区域的粗略边界框标注。2) 教师模型：使用预训练的Segment Anything Model (SAM)作为教师模型，提供像素级别的篡改区域预测。3) 学生模型：设计一个轻量级的学生模型，用于学习教师模型的知识，并进行精细的篡改定位。4) 知识蒸馏模块：利用教师模型的预测结果，指导学生模型的训练，提高学生模型的定位精度。5) 特征融合模块：采用双重引导策略，结合长期记忆和实时观察，增强模型的定位能力。

**关键创新**：BoxPromptIML的关键创新在于：1) 提出了粗略区域标注策略，有效降低了标注成本。2) 利用知识蒸馏技术，将预训练的SAM模型的知识迁移到轻量级的学生模型，提高了模型效率。3) 引入了双重引导的特征融合模块，模拟人类的记忆机制，增强了模型的定位能力。与现有方法相比，BoxPromptIML在标注成本、定位精度和模型效率之间取得了更好的平衡。

**关键设计**：1) 粗略区域标注：使用边界框标注篡改区域，标注成本远低于像素级别标注。2) 知识蒸馏：采用像素级别的知识蒸馏损失函数，鼓励学生模型的预测结果与教师模型的预测结果一致。3) 特征融合模块：使用原型记忆网络存储常见的篡改模式，并利用注意力机制将长期记忆与实时观察进行融合。4) 轻量级学生模型：采用MobileNetV3作为学生模型的骨干网络，降低模型参数量和计算复杂度。

## 📊 实验亮点

实验结果表明，BoxPromptIML在多个数据集上取得了优异的性能。在分布内数据集上，BoxPromptIML的定位精度与全监督模型相当，但在标注成本上显著降低。在分布外数据集上，BoxPromptIML表现出更强的泛化能力，优于现有的弱监督方法。此外，轻量级学生模型具有较高的推理速度，满足实际应用的需求。

## 🎯 应用场景

该研究成果可应用于数字取证、图像安全、新闻真实性验证等领域。通过快速准确地定位图像篡改区域，可以帮助识别虚假信息，维护网络安全，保障社会稳定。未来，该技术有望应用于更广泛的图像处理任务，例如图像修复、图像编辑等。

## 📄 摘要（原文）

> Image manipulation localization (IML) faces a fundamental trade-off between minimizing annotation cost and achieving fine-grained localization accuracy. Existing fully-supervised IML methods depend heavily on dense pixel-level mask annotations, which limits scalability to large datasets or real-world deployment.In contrast, the majority of existing weakly-supervised IML approaches are based on image-level labels, which greatly reduce annotation effort but typically lack precise spatial localization. To address this dilemma, we propose BoxPromptIML, a novel weakly-supervised IML framework that effectively balances annotation cost and localization performance. Specifically, we propose a coarse region annotation strategy, which can generate relatively accurate manipulation masks at lower cost. To improve model efficiency and facilitate deployment, we further design an efficient lightweight student model, which learns to perform fine-grained localization through knowledge distillation from a fixed teacher model based on the Segment Anything Model (SAM). Moreover, inspired by the human subconscious memory mechanism, our feature fusion module employs a dual-guidance strategy that actively contextualizes recalled prototypical patterns with real-time observational cues derived from the input. Instead of passive feature extraction, this strategy enables a dynamic process of knowledge recollection, where long-term memory is adapted to the specific context of the current image, significantly enhancing localization accuracy and robustness. Extensive experiments across both in-distribution and out-of-distribution datasets show that BoxPromptIML outperforms or rivals fully-supervised models, while maintaining strong generalization, low annotation cost, and efficient deployment characteristics.

