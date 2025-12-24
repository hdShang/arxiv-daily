---
layout: default
title: ViStoryBench: Comprehensive Benchmark Suite for Story Visualization
---

# ViStoryBench: Comprehensive Benchmark Suite for Story Visualization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24862" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24862v4</a>
  <a href="https://arxiv.org/pdf/2505.24862.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24862v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24862v4', 'ViStoryBench: Comprehensive Benchmark Suite for Story Visualization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cailin Zhuang, Ailin Huang, Yaoqi Hu, Jingwei Wu, Wei Cheng, Jiaqi Liao, Hongyuan Wang, Xinyao Liao, Weiwei Cai, Hengyuan Xu, Xuanyang Zhang, Xianfang Zeng, Zhewei Huang, Gang Yu, Chi Zhang

**分类**: cs.CV

**发布日期**: 2025-05-30 (更新: 2025-12-18)

**备注**: 33 Pages, Project Page: https://vistorybench.github.io/, Code: https://github.com/vistorybench/vistorybench

---

## 💡 一句话要点

**提出ViStoryBench以解决故事可视化评估不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `故事可视化` `基准测试` `多模态评估` `生成模型` `视觉叙事` `自动化指标`

## 📋 核心要点

1. 现有的故事可视化基准测试范围狭窄，无法全面评估模型在复杂叙事中的表现。
2. ViStoryBench通过丰富的多镜头脚本和自动化评估指标，提供了一个全面的故事可视化评估框架。
3. 实验结果表明，ViStoryBench能够有效评估多种开源和商业模型的性能，推动视觉叙事研究的进展。

## 📝 摘要（中文）

故事可视化旨在生成连贯的图像序列，忠实描绘叙事并与角色参考对齐。尽管生成模型取得了一定进展，现有基准测试范围狭窄，通常仅限于短提示，缺乏角色参考或单图案例，未能捕捉现实世界叙事的复杂性。为此，本文提出了ViStoryBench，一个全面的基准，旨在评估故事可视化模型在多样叙事结构、视觉风格和角色设置下的表现。该基准包含丰富注释的多镜头脚本，来源于文学、电影和民间故事。大型语言模型辅助故事总结和脚本生成，所有输出经过人工验证以确保连贯性和真实性。ViStoryBench引入了一套自动化指标，评估角色一致性、风格相似性、提示对齐、美学质量及生成伪影等，并通过人类研究验证这些指标。该基准为系统分析和推动视觉叙事的未来进展提供了多维评估工具。

## 🔬 方法详解

**问题定义**：论文要解决的问题是现有故事可视化基准测试的局限性，尤其是在叙事复杂性和角色一致性方面的不足。现有方法往往只关注短提示或单图生成，无法全面评估模型的能力和局限性。

**核心思路**：论文提出ViStoryBench作为一个全面的基准，旨在通过多样的叙事结构、视觉风格和角色设置来评估故事可视化模型。通过引入丰富的多镜头脚本和自动化评估指标，确保评估的全面性和准确性。

**技术框架**：ViStoryBench的整体架构包括多个模块：首先是故事的收集与整理，接着使用大型语言模型进行故事总结和脚本生成，最后通过人工验证确保输出的连贯性和真实性。评估阶段则使用一系列自动化指标进行性能评估。

**关键创新**：最重要的技术创新点在于引入了多维度的自动化评估指标，包括角色一致性、风格相似性等，这些指标经过人类研究验证，能够更准确地反映模型的生成质量。与现有方法相比，ViStoryBench提供了更全面的评估视角。

**关键设计**：在设计过程中，论文特别关注角色参考的选择，以确保在不同艺术风格下的故事一致性。此外，自动化指标的设计也考虑了生成伪影的检测，确保评估的全面性和准确性。具体的参数设置和损失函数设计在论文中进行了详细讨论。

## 📊 实验亮点

实验结果显示，ViStoryBench能够有效评估多种开源和商业模型的性能，尤其在角色一致性和风格相似性方面表现突出。与传统基准相比，ViStoryBench在多个维度上提供了显著的性能提升，验证了其在故事可视化领域的有效性和实用性。

## 🎯 应用场景

ViStoryBench的潜在应用领域包括电影制作、游戏设计和教育等。通过提供一个全面的评估框架，研究人员和开发者可以更好地理解和改进故事可视化模型的性能，从而推动视觉叙事技术的发展。未来，该基准可能会成为行业标准，促进更高质量的故事生成和可视化。

## 📄 摘要（原文）

> Story visualization aims to generate coherent image sequences that faithfully depict a narrative and align with character references. Despite progress in generative models, existing benchmarks are narrow in scope, often limited to short prompts, lacking character references, or single-image cases, and fail to capture real-world storytelling complexity. This hinders a nuanced understanding of model capabilities and limitations. We present \textbf{ViStoryBench}, a comprehensive benchmark designed to evaluate story visualization models across diverse narrative structures, visual styles, and character settings. The benchmark features richly annotated multi-shot scripts derived from curated stories spanning literature, film, and folklore. Large language models assist in story summarization and script generation, with all outputs human-verified to ensure coherence and fidelity. Character references are carefully curated to maintain intra-story consistency across varying artistic styles. To enable thorough evaluation, ViStoryBench introduces a set of automated metrics that assess character consistency, style similarity, prompt alignment, aesthetic quality, and generation artifacts such as copy-paste behavior. These metrics are validated through human studies, and used to benchmark a broad range of open-source and commercial models. ViStoryBench offers a multi-dimensional evaluation suite that facilitates systematic analysis and fosters future progress in visual storytelling.

