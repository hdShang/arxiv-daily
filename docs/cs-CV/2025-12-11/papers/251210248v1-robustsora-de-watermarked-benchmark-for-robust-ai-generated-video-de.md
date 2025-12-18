---
layout: default
title: RobustSora: De-Watermarked Benchmark for Robust AI-Generated Video Detection
---

# RobustSora: De-Watermarked Benchmark for Robust AI-Generated Video Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.10248" class="toolbar-btn" target="_blank">📄 arXiv: 2512.10248v1</a>
  <a href="https://arxiv.org/pdf/2512.10248.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10248v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.10248v1', 'RobustSora: De-Watermarked Benchmark for Robust AI-Generated Video Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhuo Wang, Xiliang Liu, Ligang Sun

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-11

---

## 💡 一句话要点

**RobustSora：提出去水印基准测试，评估AI生成视频检测的鲁棒性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `AI生成视频检测` `数字水印` `鲁棒性评估` `基准测试` `深度学习` `Transformer` `多模态学习`

## 📋 核心要点

1. 现有AIGC视频检测基准忽略了生成模型中数字水印的影响，导致检测器可能过度依赖水印。
2. RobustSora基准通过构建包含带水印、去水印和伪造水印的真实/生成视频数据集，评估检测器的水印鲁棒性。
3. 实验表明，现有检测器在水印操纵下性能下降2-8个百分点，突出了水印依赖问题，并为水印感知训练提供了方向。

## 📝 摘要（中文）

AI生成视频技术的快速发展对信息完整性构成了挑战。虽然最近的基准测试推动了AIGC视频检测的发展，但它们忽略了一个关键因素：许多先进的生成模型在输出中嵌入了数字水印，检测器可能部分依赖于这些模式。为了评估这种影响，我们提出了RobustSora，该基准旨在评估AIGC视频检测中的水印鲁棒性。我们系统地构建了一个包含6500个视频的数据集，包括四种类型：真实-干净（A-C）、真实-伪造水印（A-S）、生成-带水印（G-W）和生成-去水印（G-DeW）。我们的基准引入了两个评估任务：任务I测试在去除水印的AI视频上的性能，而任务II评估在带有伪造水印的真实视频上的误报率。对十个模型（包括专门的AIGC检测器、Transformer架构和MLLM方法）的实验表明，在水印操纵下，性能变化为2-8个百分点。基于Transformer的模型表现出一致的中等依赖性（6-8个百分点），而MLLM表现出不同的模式（2-8个百分点）。这些发现表明存在部分水印依赖性，并强调了水印感知训练策略的必要性。RobustSora为推进鲁棒的AIGC检测研究提供了必要的工具。

## 🔬 方法详解

**问题定义**：现有AIGC视频检测方法可能过度依赖AI生成模型嵌入的数字水印，导致在去除水印或存在伪造水印时性能显著下降。因此，需要评估和提升AIGC视频检测模型在水印干扰下的鲁棒性。现有基准测试未能充分考虑这一问题。

**核心思路**：通过构建一个包含多种水印情况（带水印、去水印、伪造水印）的AIGC视频数据集，系统地评估现有检测模型在不同水印条件下的性能表现，从而揭示模型对水印的依赖程度，并为后续研究提供基准。

**技术框架**：RobustSora基准包含一个包含6500个视频的数据集，分为四类：Authentic-Clean (A-C), Authentic-Spoofed (A-S), Generated-Watermarked (G-W), 和 Generated-DeWatermarked (G-DeW)。基准测试包含两个任务：Task-I评估模型在去水印AI生成视频上的检测性能；Task-II评估模型在带有伪造水印的真实视频上的误报率。通过在这两个任务上的表现，可以全面评估模型的水印鲁棒性。

**关键创新**：RobustSora的核心创新在于其数据集的设计，它系统地考虑了水印的存在与否以及真伪，从而能够更准确地评估AIGC视频检测模型的水印鲁棒性。与以往的基准测试相比，RobustSora更关注实际应用中可能遇到的水印干扰情况。

**关键设计**：数据集的构建需要仔细控制各类视频的比例，确保各类水印情况都有足够的样本。评估指标的选择需要能够反映模型在不同水印条件下的检测准确率和误报率。论文中使用了常见的分类指标，如准确率和召回率，以及误报率等。此外，选择具有代表性的AIGC检测模型进行评估，包括专门的AIGC检测器、Transformer架构和MLLM方法。

## 📊 实验亮点

实验结果表明，现有AIGC检测模型在RobustSora基准测试中，受到水印操纵的影响，性能下降2-8个百分点。Transformer架构的模型表现出较为一致的水印依赖性（6-8个百分点），而MLLM模型则表现出不同的模式（2-8个百分点）。这些结果突出了现有模型对水印的依赖，并验证了RobustSora基准测试的有效性。

## 🎯 应用场景

RobustSora基准测试可用于评估和提升AIGC视频检测模型的鲁棒性，尤其是在水印干扰下的性能。这对于打击AI生成虚假信息、保护知识产权、维护网络安全具有重要意义。未来的研究可以基于RobustSora开发更有效的水印感知检测方法，提高AIGC内容识别的可靠性。

## 📄 摘要（原文）

> The proliferation of AI-generated video technologies poses challenges to information integrity. While recent benchmarks advance AIGC video detection, they overlook a critical factor: many state-of-the-art generative models embed digital watermarks in outputs, and detectors may partially rely on these patterns. To evaluate this influence, we present RobustSora, the benchmark designed to assess watermark robustness in AIGC video detection. We systematically construct a dataset of 6,500 videos comprising four types: Authentic-Clean (A-C), Authentic-Spoofed with fake watermarks (A-S), Generated-Watermarked (G-W), and Generated-DeWatermarked (G-DeW). Our benchmark introduces two evaluation tasks: Task-I tests performance on watermark-removed AI videos, while Task-II assesses false alarm rates on authentic videos with fake watermarks. Experiments with ten models spanning specialized AIGC detectors, transformer architectures, and MLLM approaches reveal performance variations of 2-8pp under watermark manipulation. Transformer-based models show consistent moderate dependency (6-8pp), while MLLMs exhibit diverse patterns (2-8pp). These findings indicate partial watermark dependency and highlight the need for watermark-aware training strategies. RobustSora provides essential tools to advance robust AIGC detection research.

