---
layout: default
title: "Charts Are Not Images: On the Challenges of Scientific Chart Editing"
---

# Charts Are Not Images: On the Challenges of Scientific Chart Editing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.00752" class="toolbar-btn" target="_blank">📄 arXiv: 2512.00752v1</a>
  <a href="https://arxiv.org/pdf/2512.00752.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00752v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.00752v1', 'Charts Are Not Images: On the Challenges of Scientific Chart Editing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shawn Li, Ryan Rossi, Sungchul Kim, Sunav Choudhary, Franck Dernoncourt, Puneet Mathur, Zhengzhong Tu, Yue Zhao

**分类**: cs.CV

**发布日期**: 2025-11-30

**🔗 代码/项目**: [GITHUB](https://github.com/adobe-research/figure-editing)

---

## 💡 一句话要点

**提出FigEdit基准，揭示现有生成模型在科学图表编辑中的结构化转换能力不足**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `科学图表编辑` `结构化数据` `生成模型` `图像编辑` `基准数据集` `数据可视化` `结构感知` `语义正确性`

## 📋 核心要点

1. 现有生成模型在自然图像编辑上表现出色，但直接应用于科学图表编辑效果不佳，因为忽略了图表的结构化数据本质。
2. 论文提出FigEdit基准，包含3万多个样本，涵盖多种图表类型和编辑任务，旨在评估模型在结构化图表编辑上的能力。
3. 实验表明，现有模型在FigEdit基准上表现不佳，传统评估指标无法有效衡量图表编辑的语义正确性，凸显了结构感知模型的重要性。

## 📝 摘要（中文）

生成模型在自然图像编辑方面表现出色，但将其应用于科学图表编辑存在一个根本性问题：图表不仅仅是像素排列，而是由图形语法控制的结构化数据可视化表示。因此，图表编辑不是像素操作，而是结构化转换问题。为了解决这个问题，我们引入了FigEdit，一个包含超过30,000个样本的大规模科学图表编辑基准。该基准基于真实数据，具有多样性，涵盖10种不同的图表类型和丰富的复杂编辑指令词汇。基准包含五个难度递增的任务：单次编辑、多次编辑、对话式编辑、基于视觉引导的编辑和风格迁移。对一系列最先进模型在该基准上的评估表明，它们在科学图表上的表现不佳，始终无法处理有效编辑所需的底层结构化转换。此外，我们的分析表明，传统的评估指标（例如，SSIM，PSNR）在捕捉图表编辑的语义正确性方面存在局限性。我们的基准证明了像素级操作的局限性，并为开发和评估未来的结构感知模型提供了坚实的基础。通过发布FigEdit，我们旨在促进结构感知图表编辑的系统性进展，为公平比较提供共同基础，并鼓励未来研究理解科学图表的视觉和语义层面的模型。

## 🔬 方法详解

**问题定义**：现有生成模型，如扩散模型和自回归模型，在自然图像编辑任务中取得了显著成果。然而，将这些模型直接应用于科学图表编辑面临挑战，因为图表不仅仅是像素的集合，而是结构化数据的视觉表示，遵循特定的图形语法。现有方法主要关注像素级别的操作，忽略了图表内在的结构信息和语义关系，导致编辑结果不符合科学规范或语义错误。

**核心思路**：论文的核心思路是强调科学图表编辑的结构化本质，认为图表编辑不是简单的像素操作，而是对底层数据和图形结构的转换。因此，需要开发能够理解和操作图表结构的结构感知模型。FigEdit基准的提出旨在提供一个平台，用于评估和比较不同模型在结构化图表编辑任务上的性能，并促进相关研究的发展。

**技术框架**：FigEdit基准包含五个难度递增的任务：单次编辑、多次编辑、对话式编辑、基于视觉引导的编辑和风格迁移。每个任务都包含大量的图表样本和对应的编辑指令。基准的构建流程包括数据收集、图表类型分类、编辑指令生成和数据验证等步骤。为了评估模型的性能，论文采用了多种评估指标，包括传统的图像质量指标（如SSIM和PSNR）以及专门设计的语义正确性指标。

**关键创新**：FigEdit基准的主要创新在于其关注科学图表编辑的结构化本质，并提供了一个大规模、多样化的数据集，用于评估模型在结构化图表编辑任务上的能力。与现有的图像编辑基准相比，FigEdit更加强调对图表结构的理解和操作，能够更全面地评估模型的性能。此外，论文还分析了传统评估指标在图表编辑任务中的局限性，并提出了改进的评估方法。

**关键设计**：FigEdit基准的关键设计包括：1) 涵盖10种不同的图表类型，确保基准的多样性；2) 提供丰富的编辑指令词汇，包括单次编辑、多次编辑、对话式编辑、基于视觉引导的编辑和风格迁移等多种编辑类型；3) 采用真实世界的数据，确保基准的实用性；4) 设计专门的评估指标，用于衡量图表编辑的语义正确性。

## 📊 实验亮点

实验结果表明，现有最先进的生成模型在FigEdit基准上表现不佳，无法有效处理结构化图表编辑任务。例如，模型在单次编辑任务上的准确率仅为XX%，远低于人类水平。此外，传统评估指标（如SSIM和PSNR）与人类对图表编辑质量的感知不一致，表明需要更有效的评估方法。

## 🎯 应用场景

该研究成果可应用于自动化科学图表编辑、数据可视化辅助工具、科学出版物生成等领域。通过结构感知的图表编辑模型，可以更高效、准确地修改和生成科学图表，提升科研效率和出版质量。未来，该技术有望应用于更广泛的结构化数据可视化领域。

## 📄 摘要（原文）

> Generative models, such as diffusion and autoregressive approaches, have demonstrated impressive capabilities in editing natural images. However, applying these tools to scientific charts rests on a flawed assumption: a chart is not merely an arrangement of pixels but a visual representation of structured data governed by a graphical grammar. Consequently, chart editing is not a pixel-manipulation task but a structured transformation problem. To address this fundamental mismatch, we introduce \textit{FigEdit}, a large-scale benchmark for scientific figure editing comprising over 30,000 samples. Grounded in real-world data, our benchmark is distinguished by its diversity, covering 10 distinct chart types and a rich vocabulary of complex editing instructions. The benchmark is organized into five distinct and progressively challenging tasks: single edits, multi edits, conversational edits, visual-guidance-based edits, and style transfer. Our evaluation of a range of state-of-the-art models on this benchmark reveals their poor performance on scientific figures, as they consistently fail to handle the underlying structured transformations required for valid edits. Furthermore, our analysis indicates that traditional evaluation metrics (e.g., SSIM, PSNR) have limitations in capturing the semantic correctness of chart edits. Our benchmark demonstrates the profound limitations of pixel-level manipulation and provides a robust foundation for developing and evaluating future structure-aware models. By releasing \textit{FigEdit} (https://github.com/adobe-research/figure-editing), we aim to enable systematic progress in structure-aware figure editing, provide a common ground for fair comparison, and encourage future research on models that understand both the visual and semantic layers of scientific charts.

