---
layout: default
title: "TurnBack: A Geospatial Route Cognition Benchmark for Large Language Models through Reverse Route"
---

# TurnBack: A Geospatial Route Cognition Benchmark for Large Language Models through Reverse Route

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18173" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18173v1</a>
  <a href="https://arxiv.org/pdf/2509.18173.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18173v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18173v1', 'TurnBack: A Geospatial Route Cognition Benchmark for Large Language Models through Reverse Route')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongyi Luo, Qing Cheng, Daniel Matos, Hari Krishna Gadi, Yanfeng Zhang, Lu Liu, Yongliang Wang, Niclas Zeller, Daniel Cremers, Liqiu Meng

**分类**: cs.LG, cs.CL

**发布日期**: 2025-09-17

**备注**: Accepted to EMNLP 2025 (Main). This is the camera-ready/author version

**🔗 代码/项目**: [GITHUB](https://github.com/bghjmn32/EMNLP2025_Turnback)

---

## 💡 一句话要点

**提出TurnBack基准，评估大语言模型在逆向地理空间路径认知方面的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `地理空间认知` `路径规划` `逆向路径` `基准测试`

## 📋 核心要点

1. 现有研究缺乏可量化的指标和大规模数据集，难以充分评估大语言模型在地理空间认知方面的能力。
2. 论文提出TurnBack基准和PathBuilder工具，用于生成和评估LLMs的逆向地理空间路径认知能力。
3. 实验表明，LLMs在逆向路径任务中表现出局限性，存在鲁棒性低和过度自信等问题。

## 📝 摘要（中文）

本文提出了一项大规模基准测试，旨在全面评估大语言模型（LLMs）的地理空间路径认知能力。尽管人类可以通过自然语言理解地理空间信息，但LLMs在这方面的能力仍有待探索。现有研究受限于不可量化的指标、有限的评估数据集和不明确的研究层级。为此，我们构建了一个包含来自全球12个大都市的36000条路径的大规模评估数据集。此外，我们引入了PathBuilder，一种用于将自然语言指令转换为导航路线，反之亦然的新工具，从而弥合了地理空间信息和自然语言之间的差距。最后，我们提出了一个新的评估框架和指标，以严格评估11个最先进的LLMs在路径逆转任务上的表现。基准测试表明，LLMs在逆向路径方面存在局限性：大多数逆向路径既没有返回起点，也与最佳路径相似。此外，LLMs在路线生成方面面临鲁棒性低以及对其不正确答案的高度自信等挑战。

## 🔬 方法详解

**问题定义**：论文旨在解决大语言模型（LLMs）在地理空间路径认知方面的评估问题，特别是逆向路径认知能力。现有方法缺乏标准化的评估基准和可量化的指标，难以准确衡量LLMs在此方面的能力。此外，现有数据集规模有限，无法充分覆盖各种复杂的地理空间场景。

**核心思路**：论文的核心思路是构建一个大规模的逆向路径评估基准，通过将自然语言描述的路径转换为地理坐标，并反向生成自然语言描述，来评估LLMs对地理空间信息的理解和推理能力。PathBuilder工具的引入，旨在弥合自然语言和地理空间信息之间的鸿沟。

**技术框架**：整体框架包含三个主要部分：1) 大规模数据集构建，包含来自12个大都市的36000条路径；2) PathBuilder工具，用于自然语言路径描述和地理坐标之间的转换；3) 评估框架，包括新的评估指标和对11个SOTA LLMs的评估。PathBuilder工具能够将自然语言指令转换为导航路线，也能将导航路线反向生成自然语言描述。

**关键创新**：论文的关键创新在于提出了TurnBack基准，这是一个大规模、可量化的地理空间路径认知评估框架。PathBuilder工具的引入，使得自然语言和地理空间信息之间的转换成为可能，从而能够更全面地评估LLMs的地理空间认知能力。与现有方法相比，TurnBack基准提供了更丰富的评估数据和更严格的评估指标。

**关键设计**：PathBuilder工具的设计细节未知，但其核心功能是实现自然语言路径描述和地理坐标之间的双向转换。评估指标的设计旨在衡量LLMs生成的逆向路径与原始路径的相似度，以及是否能够返回起点。具体的损失函数和网络结构等技术细节在论文中未明确说明。

## 📊 实验亮点

实验结果表明，现有的SOTA LLMs在逆向路径任务中表现出明显的局限性，大多数逆向路径既没有返回起点，也与最佳路径相似度较低。此外，LLMs在路线生成方面鲁棒性较差，并且对其不正确的答案表现出高度自信。这些发现揭示了LLMs在地理空间认知方面存在的挑战，为未来的研究提供了方向。

## 🎯 应用场景

该研究成果可应用于智能导航、自动驾驶、地理信息系统等领域。通过提升LLMs的地理空间认知能力，可以改善导航系统的用户体验，提高自动驾驶车辆的路径规划能力，并为地理信息系统的智能化提供支持。未来的研究可以进一步探索如何利用LLMs进行更复杂的地理空间推理和决策。

## 📄 摘要（原文）

> Humans can interpret geospatial information through natural language, while the geospatial cognition capabilities of Large Language Models (LLMs) remain underexplored. Prior research in this domain has been constrained by non-quantifiable metrics, limited evaluation datasets and unclear research hierarchies. Therefore, we propose a large-scale benchmark and conduct a comprehensive evaluation of the geospatial route cognition of LLMs. We create a large-scale evaluation dataset comprised of 36000 routes from 12 metropolises worldwide. Then, we introduce PathBuilder, a novel tool for converting natural language instructions into navigation routes, and vice versa, bridging the gap between geospatial information and natural language. Finally, we propose a new evaluation framework and metrics to rigorously assess 11 state-of-the-art (SOTA) LLMs on the task of route reversal. The benchmark reveals that LLMs exhibit limitation to reverse routes: most reverse routes neither return to the starting point nor are similar to the optimal route. Additionally, LLMs face challenges such as low robustness in route generation and high confidence for their incorrect answers. Code\ \&\ Data available here: \href{https://github.com/bghjmn32/EMNLP2025_Turnback}{TurnBack.}

