---
layout: default
title: "FOCUS: Internal MLLM Representations for Efficient Fine-Grained Visual Question Answering"
---

# FOCUS: Internal MLLM Representations for Efficient Fine-Grained Visual Question Answering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21710" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21710v2</a>
  <a href="https://arxiv.org/pdf/2506.21710.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21710v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21710v2', 'FOCUS: Internal MLLM Representations for Efficient Fine-Grained Visual Question Answering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liangyu Zhong, Fabio Rosenthal, Joachim Sicking, Fabian Hüger, Thorsten Bagdonat, Hanno Gottschalk, Leo Schwinn

**分类**: cs.CV

**发布日期**: 2025-06-26 (更新: 2025-10-29)

**备注**: Accepted by NeurIPS 2025 - main track. Project page: https://focus-mllm-vqa.github.io/

---

## 💡 一句话要点

**提出FOCUS以解决细粒度视觉问答中的视觉裁剪问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉问答` `多模态大语言模型` `视觉裁剪` `细粒度识别` `对象相关性图`

## 📋 核心要点

1. 现有的视觉问答方法在处理小图像细节时效率低下，且需要任务特定的微调。
2. FOCUS通过无训练的视觉裁剪方法，利用MLLM内部表示来优化图像区域搜索过程。
3. FOCUS在多个细粒度VQA数据集上表现优异，超越了传统方法，并显著降低计算需求。

## 📝 摘要（中文）

尽管多模态大语言模型（MLLMs）在图像-文本输入的感知和推理能力上表现出色，但在关注小图像细节的视觉问答（VQA）中仍然面临挑战。现有的视觉裁剪技术存在任务特定微调需求、低效率和与高效注意力实现不兼容等限制。为了解决这些问题，本文提出了一种无训练的视觉裁剪方法FOCUS，利用MLLM内部表示来指导最相关图像区域的搜索。FOCUS通过四个步骤实现：首先识别VQA提示中的目标对象；其次，使用键值（KV）缓存计算对象相关性图；然后，根据该图提出并排名相关图像区域；最后，使用排名最高的区域执行细粒度VQA任务。FOCUS在四个细粒度VQA数据集和三种类型的MLLM上表现出色，超越了三种流行的视觉裁剪方法，并在计算效率上要求减少3到6.5倍。

## 🔬 方法详解

**问题定义**：本文旨在解决细粒度视觉问答中对小图像细节的处理问题。现有方法面临的痛点包括任务特定微调的需求、低效率的无信息搜索以及与高效注意力实现的不兼容性。

**核心思路**：FOCUS的核心思路是利用MLLM内部表示进行无训练的视觉裁剪，优化相关图像区域的搜索过程。通过这种方式，FOCUS能够在不需要额外训练的情况下，提升VQA任务的效率和准确性。

**技术框架**：FOCUS的整体架构包括四个主要步骤：首先识别VQA提示中的目标对象；其次计算对象相关性图；然后根据该图提出并排名相关图像区域；最后执行细粒度VQA任务。

**关键创新**：FOCUS的主要创新在于其无训练的视觉裁剪方法，利用MLLM内部的键值缓存进行对象相关性计算，这一设计使得FOCUS在效率和准确性上超越了现有的视觉裁剪方法。

**关键设计**：FOCUS的关键设计包括使用键值缓存来生成对象相关性图，以及基于该图进行图像区域的排名。这些设计使得FOCUS在计算上更为高效，且能够在多个数据集上取得优异的表现。

## 📊 实验亮点

FOCUS在四个细粒度VQA数据集上表现出色，超越了三种流行的视觉裁剪方法，且在计算效率上要求减少3到6.5倍。其性能与最佳基线ZoomEye相当，显示出其在准确性和效率上的显著提升。

## 🎯 应用场景

FOCUS的研究成果在多个领域具有潜在应用价值，包括智能问答系统、图像检索和人机交互等。通过提升细粒度视觉问答的效率和准确性，该方法能够为用户提供更为精准的信息检索和交互体验，推动相关技术的发展与应用。

## 📄 摘要（原文）

> While Multimodal Large Language Models (MLLMs) offer strong perception and reasoning capabilities for image-text input, Visual Question Answering (VQA) focusing on small image details still remains a challenge. Although visual cropping techniques seem promising, recent approaches have several limitations: the need for task-specific fine-tuning, low efficiency due to uninformed exhaustive search, or incompatibility with efficient attention implementations. We address these shortcomings by proposing a training-free visual cropping method, dubbed FOCUS, that leverages MLLM-internal representations to guide the search for the most relevant image region. This is accomplished in four steps: first, we identify the target object(s) in the VQA prompt; second, we compute an object relevance map using the key-value (KV) cache; third, we propose and rank relevant image regions based on the map; and finally, we perform the fine-grained VQA task using the top-ranked region. As a result of this informed search strategy, FOCUS achieves strong performance across four fine-grained VQA datasets and three types of MLLMs. It outperforms three popular visual cropping methods in both accuracy and efficiency, and matches the best-performing baseline, ZoomEye, while requiring 3 - 6.5 x less compute.

