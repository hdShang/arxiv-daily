---
layout: default
title: OmniGenBench: A Modular Platform for Reproducible Genomic Foundation Models Benchmarking
---

# OmniGenBench: A Modular Platform for Reproducible Genomic Foundation Models Benchmarking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14402" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14402v1</a>
  <a href="https://arxiv.org/pdf/2505.14402.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14402v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14402v1', 'OmniGenBench: A Modular Platform for Reproducible Genomic Foundation Models Benchmarking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Heng Yang, Jack Cole, Yuan Li, Renzhi Chen, Geyong Min, Ke Li

**分类**: q-bio.GN, cs.CL

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出OmniGenBench以解决基因组基础模型评估的可重复性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `基因组学` `基础模型` `可重复性` `模块化平台` `AI评估` `数据透明性` `模型互操作性`

## 📋 核心要点

1. 现有的基因组基础模型评估缺乏标准化和可重复性，导致研究结果难以验证和比较。
2. OmniGenBench通过模块化设计，统一了数据、模型和评估流程，实现了对GFM的标准化评估。
3. 该平台集成了31个开源模型，提供自动化评估管道，显著提升了基因组AI研究的可重复性和透明性。

## 📝 摘要（中文）

自然界的代码，嵌入在DNA和RNA基因组中，自生命起源以来，蕴含着巨大的潜力，能够通过基因组建模影响人类和生态系统。基因组基础模型（GFM）作为解码基因组的变革性方法，正在迅速发展。然而，随着GFM的规模扩大，AI驱动的基因组学领域面临着严格且可重复评估的迫切需求。我们提出了OmniGenBench，一个模块化的基准测试平台，旨在统一GFM的数据、模型、基准测试和可解释性层面。OmniGenBench支持通过单一命令对任何GFM进行标准化评估，并无缝集成超过31个开源模型。通过自动化管道和社区可扩展功能，该平台解决了数据透明性、模型互操作性、基准测试碎片化和黑箱可解释性等关键的可重复性挑战。OmniGenBench旨在为可重复的基因组AI研究提供基础设施，加速可信发现和协作创新。

## 🔬 方法详解

**问题定义**：论文要解决的问题是基因组基础模型（GFM）评估的可重复性和标准化不足，现有方法在数据透明性、模型互操作性和评估一致性方面存在显著挑战。

**核心思路**：论文提出的核心思路是构建一个模块化的基准测试平台OmniGenBench，旨在通过统一的数据和模型接口，简化GFM的评估流程，提升研究的可重复性和透明性。

**技术框架**：OmniGenBench的整体架构包括数据层、模型层、基准测试层和可解释性层，支持通过单一命令对多种GFM进行评估，并能够与多个开源模型无缝集成。

**关键创新**：最重要的技术创新点在于其模块化设计和自动化评估管道，解决了传统评估方法中存在的碎片化问题，使得不同模型之间的比较更加高效和可靠。

**关键设计**：在设计上，OmniGenBench采用了标准化的数据格式和接口，支持多种模型的输入输出，同时提供了灵活的参数设置和损失函数选择，以适应不同的基因组学任务。

## 📊 实验亮点

在实验中，OmniGenBench成功集成了超过31个开源模型，并通过单一命令实现了对不同GFM的标准化评估。与传统方法相比，该平台在数据透明性和模型互操作性方面显著提升，解决了基因组AI研究中的关键可重复性问题。

## 🎯 应用场景

OmniGenBench的潜在应用领域包括基因组学研究、个性化医疗、生态系统监测等。通过提供一个标准化的评估平台，该研究能够加速基因组AI技术的开发与应用，推动科学发现和技术创新。未来，OmniGenBench有望成为基因组学领域的基础设施，促进跨学科的合作与研究。

## 📄 摘要（原文）

> The code of nature, embedded in DNA and RNA genomes since the origin of life, holds immense potential to impact both humans and ecosystems through genome modeling. Genomic Foundation Models (GFMs) have emerged as a transformative approach to decoding the genome. As GFMs scale up and reshape the landscape of AI-driven genomics, the field faces an urgent need for rigorous and reproducible evaluation. We present OmniGenBench, a modular benchmarking platform designed to unify the data, model, benchmarking, and interpretability layers across GFMs. OmniGenBench enables standardized, one-command evaluation of any GFM across five benchmark suites, with seamless integration of over 31 open-source models. Through automated pipelines and community-extensible features, the platform addresses critical reproducibility challenges, including data transparency, model interoperability, benchmark fragmentation, and black-box interpretability. OmniGenBench aims to serve as foundational infrastructure for reproducible genomic AI research, accelerating trustworthy discovery and collaborative innovation in the era of genome-scale modeling.

