---
layout: default
title: "CLAMP: Crowdsourcing a LArge-scale in-the-wild haptic dataset with an open-source device for Multimodal robot Perception"
---

# CLAMP: Crowdsourcing a LArge-scale in-the-wild haptic dataset with an open-source device for Multimodal robot Perception

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21495" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21495v1</a>
  <a href="https://arxiv.org/pdf/2505.21495.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21495v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21495v1', 'CLAMP: Crowdsourcing a LArge-scale in-the-wild haptic dataset with an open-source device for Multimodal robot Perception')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pranav N. Thakkar, Shubhangi Sinha, Karan Baijal, Yuhan, Bian, Leah Lackey, Ben Dodson, Heisen Kong, Jueun Kwon, Amber Li, Yifei Hu, Alexios Rekoutis, Tom Silver, Tapomayukh Bhattacharjee

**分类**: cs.RO

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出CLAMP设备以解决大规模触觉数据集缺乏问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态触觉` `机器人操作` `数据集构建` `材料识别` `触觉传感器`

## 📋 核心要点

1. 现有的机器人操作方法在理解物体的材料和顺应性属性方面存在局限，主要依赖视觉信息，难以应对复杂的现实场景。
2. 本文提出了CLAMP设备，通过低成本的传感器化抓取器收集多模态触觉数据，形成了一个大规模的开源数据集，以支持机器人对物体属性的理解。
3. 实验结果表明，使用CLAMP数据集训练的模型在材料识别和实际操作任务中表现出色，能够有效推广到新物体和不同的机器人形态。

## 📝 摘要（中文）

在非结构化环境中，机器人操作的稳健性通常需要理解超越几何的物体属性，如材料或顺应性，这些属性仅通过视觉难以推断。多模态触觉传感提供了一条有前景的途径，但由于缺乏大型、多样化和真实的触觉数据集，进展受到限制。本文介绍了CLAMP设备，这是一种低成本（<200美元）的传感器化抓取器，旨在从非专业用户的日常环境中收集大规模的多模态触觉数据。我们部署了16个CLAMP设备，参与者达41人，最终形成了CLAMP数据集，这是迄今为止最大的开源多模态触觉数据集，包含1230万个数据点和5357个家庭物体。利用该数据集，我们训练了一个触觉编码器，可以从多模态触觉数据中推断材料和顺应性属性，并创建了CLAMP模型，这是一种用于材料识别的视觉-触觉感知模型，能够在最小微调的情况下推广到新物体和三种机器人形态。我们还展示了该模型在三项实际机器人操作任务中的有效性：分类可回收和不可回收的废物、从杂乱的包中检索物体，以及区分过熟和成熟的香蕉。我们的结果表明，大规模的触觉数据收集可以解锁机器人操作的新能力。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在非结构化环境中对物体材料和顺应性属性理解不足的问题。现有方法主要依赖视觉信息，难以准确推断物体的触觉特性，限制了机器人操作的灵活性和准确性。

**核心思路**：论文提出了一种低成本的CLAMP设备，旨在通过收集多模态触觉数据来增强机器人对物体属性的理解。该设备的设计考虑了非专业用户的使用场景，使得大规模数据收集成为可能。

**技术框架**：整体架构包括CLAMP设备的设计、数据收集、触觉编码器的训练和CLAMP模型的构建。数据收集阶段涉及16个设备和41名参与者，触觉编码器用于从数据中提取物体属性，最终形成的CLAMP模型用于实际操作任务。

**关键创新**：CLAMP设备的设计和大规模数据集的构建是本研究的核心创新。与现有方法相比，CLAMP能够有效收集多样化的触觉数据，支持更广泛的机器人操作任务。

**关键设计**：在模型训练中，采用了特定的损失函数以优化触觉特征的提取，网络结构设计上考虑了多模态输入的融合，确保了模型在新物体和不同机器人形态上的良好泛化能力。

## 📊 实验亮点

实验结果显示，CLAMP模型在材料识别任务中表现优异，能够在最小微调的情况下推广到新物体和三种不同的机器人形态。具体而言，模型在分类可回收与不可回收废物、从杂乱包中检索物体以及区分过熟与成熟香蕉的任务中均取得了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、服务机器人和工业自动化等。通过增强机器人对物体属性的理解，CLAMP模型可以提升机器人在复杂环境中的操作能力，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Robust robot manipulation in unstructured environments often requires understanding object properties that extend beyond geometry, such as material or compliance-properties that can be challenging to infer using vision alone. Multimodal haptic sensing provides a promising avenue for inferring such properties, yet progress has been constrained by the lack of large, diverse, and realistic haptic datasets. In this work, we introduce the CLAMP device, a low-cost (<\$200) sensorized reacher-grabber designed to collect large-scale, in-the-wild multimodal haptic data from non-expert users in everyday settings. We deployed 16 CLAMP devices to 41 participants, resulting in the CLAMP dataset, the largest open-source multimodal haptic dataset to date, comprising 12.3 million datapoints across 5357 household objects. Using this dataset, we train a haptic encoder that can infer material and compliance object properties from multimodal haptic data. We leverage this encoder to create the CLAMP model, a visuo-haptic perception model for material recognition that generalizes to novel objects and three robot embodiments with minimal finetuning. We also demonstrate the effectiveness of our model in three real-world robot manipulation tasks: sorting recyclable and non-recyclable waste, retrieving objects from a cluttered bag, and distinguishing overripe from ripe bananas. Our results show that large-scale, in-the-wild haptic data collection can unlock new capabilities for generalizable robot manipulation. Website: https://emprise.cs.cornell.edu/clamp/

