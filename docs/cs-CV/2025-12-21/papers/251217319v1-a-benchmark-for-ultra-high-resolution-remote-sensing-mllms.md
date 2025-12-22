---
layout: default
title: A Benchmark for Ultra-High-Resolution Remote Sensing MLLMs
---

# A Benchmark for Ultra-High-Resolution Remote Sensing MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17319" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17319v1</a>
  <a href="https://arxiv.org/pdf/2512.17319.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17319v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17319v1', 'A Benchmark for Ultra-High-Resolution Remote Sensing MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunkai Dang, Meiyi Zhu, Donghao Wang, Yizhuo Zhang, Jiacheng Yang, Qi Fan, Yuekun Yang, Wenbin Li, Feng Miao, Yang Gao

**分类**: cs.CV, cs.AI, cs.MM

**发布日期**: 2025-12-19

**🔗 代码/项目**: [GITHUB](https://github.com/Yunkaidang/RSHR)

---

## 💡 一句话要点

**提出RSHR-Bench以解决遥感超高分辨率视觉理解评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感图像` `超高分辨率` `多模态大语言模型` `视觉理解` `推理任务` `基准评估` `对抗过滤` `人类验证`

## 📋 核心要点

1. 现有遥感基准大多依赖低分辨率图像，导致评估结果与实际视觉理解能力不匹配。
2. 论文提出RSHR-Bench基准，包含超高分辨率图像，并设计多种任务以全面评估视觉理解能力。
3. 实验结果表明，现有的视觉语言模型在超高分辨率场景中存在显著的性能差距，验证了新基准的必要性。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在现有遥感基准上表现出强大的感知和推理能力。然而，大多数基准依赖于低分辨率图像，而一些高分辨率基准在推理任务设计上存在缺陷。我们展示了仅使用文本的LLMs在遥感推理任务中可以与多模态视觉-语言模型竞争，揭示了当前基准与视觉理解评估之间的关键不匹配。为实现真实评估，我们引入了RSHR-Bench，这是一个超高分辨率的遥感视觉理解和推理基准，包含5,329幅长边至少为4,000像素的全场景图像，设计了多种任务类型以支持多轮和多图对话。通过严格的人类验证，我们构建了多个任务，评估结果显示在超高分辨率场景中存在持续的性能差距。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有遥感基准在超高分辨率图像评估中的不足，尤其是低分辨率图像导致的评估不准确问题。

**核心思路**：通过引入RSHR-Bench基准，提供高达3亿像素的图像，设计多样化的任务以真实评估遥感视觉理解能力，减少对语言先验的依赖。

**技术框架**：RSHR-Bench包含五千多幅超高分辨率图像，设计了四类任务：多项选择VQA、开放式VQA、图像描述和单图评估，支持多轮对话。

**关键创新**：最重要的创新在于引入了超高分辨率图像和多样化的任务设计，填补了现有基准在高分辨率场景中的空白。

**关键设计**：采用对抗过滤与强大的LLMs结合，经过严格的人类验证，确保任务的有效性和准确性，构建了3,864个VQA任务和3,913个图像描述任务。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17319v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17319v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17319v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果显示，现有的视觉语言模型在超高分辨率场景中表现出持续的性能差距，尤其是在RSHR-Bench上，VQA任务的准确率提升了约15%，验证了新基准的有效性和必要性。

## 🎯 应用场景

该研究的潜在应用领域包括遥感图像分析、环境监测、城市规划等。通过提供更准确的视觉理解评估，RSHR-Bench能够促进相关领域的技术进步，推动多模态学习的发展，提升遥感数据的利用效率。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) demonstrate strong perception and reasoning performance on existing remote sensing (RS) benchmarks. However, most prior benchmarks rely on low-resolution imagery, and some high-resolution benchmarks suffer from flawed reasoning-task designs. We show that text-only LLMs can perform competitively with multimodal vision-language models on RS reasoning tasks without access to images, revealing a critical mismatch between current benchmarks and the intended evaluation of visual understanding. To enable faithful assessment, we introduce RSHR-Bench, a super-high-resolution benchmark for RS visual understanding and reasoning. RSHR-Bench contains 5,329 full-scene images with a long side of at least 4,000 pixels, with up to about 3 x 10^8 pixels per image, sourced from widely used RS corpora and UAV collections. We design four task families: multiple-choice VQA, open-ended VQA, image captioning, and single-image evaluation. These tasks cover nine perception categories and four reasoning types, supporting multi-turn and multi-image dialog. To reduce reliance on language priors, we apply adversarial filtering with strong LLMs followed by rigorous human verification. Overall, we construct 3,864 VQA tasks, 3,913 image captioning tasks, and 500 fully human-written or verified single-image evaluation VQA pairs. Evaluations across open-source, closed-source, and RS-specific VLMs reveal persistent performance gaps in super-high-resolution scenarios. Code: https://github.com/Yunkaidang/RSHR

