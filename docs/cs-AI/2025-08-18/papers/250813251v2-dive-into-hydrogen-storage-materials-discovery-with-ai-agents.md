---
layout: default
title: "\"DIVE\" into Hydrogen Storage Materials Discovery with AI Agents"
---

# "DIVE" into Hydrogen Storage Materials Discovery with AI Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13251" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13251v2</a>
  <a href="https://arxiv.org/pdf/2508.13251.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13251v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13251v2', '&quot;DIVE&quot; into Hydrogen Storage Materials Discovery with AI Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Di Zhang, Xue Jia, Tran Ba Hung, Seong Hoon Jang, Linda Zhang, Ryuhei Sato, Yusuke Hashimoto, Toyoto Sato, Kiyoe Konno, Shin-ichi Orimo, Hao Li

**分类**: cs.AI, cond-mat.mtrl-sci

**发布日期**: 2025-08-18 (更新: 2025-09-25)

**备注**: 23 pages, 5 figures. The supplementary video is available at the GitHub link provided in the manuscript

---

## 💡 一句话要点

**提出DIVE以解决氢储存材料发现中的数据提取问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `氢储存材料` `数据提取` `人工智能` `材料发现` `多代理系统`

## 📋 核心要点

1. 现有方法在提取科学文献中的材料数据时，面临大量信息被困于非结构化图形和表格的问题，导致数据利用率低。
2. 论文提出DIVE多代理工作流，通过系统性读取和组织实验数据，解决了数据提取的准确性和覆盖率问题。
3. 实验结果表明，DIVE在数据提取准确性上较商业模型提升10-15%，较开源模型提升超过30%，并能快速识别新材料组合。

## 📝 摘要（中文）

数据驱动的人工智能方法正在根本性地改变新材料的发现。尽管科学文献中材料数据的可用性前所未有，但大量信息仍被困于非结构化的图形和表格中，阻碍了基于大语言模型的自动化材料设计的构建。本文提出了描述性视觉表达解读（DIVE）多代理工作流，系统性地读取和组织科学文献中的实验数据。我们专注于固态氢储存材料，展示DIVE在数据提取的准确性和覆盖率上显著优于多模态模型，商业模型提升10-15%，开源模型提升超过30%。基于超过30,000条来自4,000篇文献的数据库，我们建立了一个快速逆向设计工作流，能够在两分钟内识别出未报告的氢储存组合。该AI工作流和代理设计在多种材料中具有广泛的可转移性，为AI驱动的材料发现提供了新范式。

## 🔬 方法详解

**问题定义**：本文旨在解决现有材料发现方法中，科学文献中的实验数据因非结构化形式而难以提取的问题。现有多模态模型在数据提取的准确性和覆盖率上存在不足。

**核心思路**：DIVE工作流通过多代理系统，系统性地解析和组织图形元素中的数据，从而提高数据提取的效率和准确性。这种设计使得AI能够更好地理解和利用科学文献中的信息。

**技术框架**：DIVE工作流包括数据读取、数据组织和数据提取三个主要模块。首先，系统读取文献中的图形元素，然后将数据进行结构化整理，最后进行高效的数据提取和分析。

**关键创新**：DIVE的核心创新在于其多代理工作流的设计，能够有效处理非结构化数据，并显著提高数据提取的准确性和覆盖率。这与传统的直接提取方法形成了鲜明对比。

**关键设计**：在DIVE中，采用了特定的参数设置和损失函数，以优化数据提取的效果。同时，设计了适合图形数据解析的网络结构，以确保高效的处理能力。通过这些技术细节，DIVE能够在短时间内完成复杂的数据提取任务。

## 📊 实验亮点

实验结果显示，DIVE在数据提取的准确性上较商业模型提升10-15%，较开源模型提升超过30%。此外，DIVE能够在两分钟内识别出未报告的氢储存组合，展现出其高效的逆向设计能力。

## 🎯 应用场景

该研究的潜在应用领域包括新材料的发现与开发，尤其是在氢储存和清洁能源技术方面。DIVE工作流的设计可以广泛应用于其他材料领域，推动材料科学的进步，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Data-driven artificial intelligence (AI) approaches are fundamentally transforming the discovery of new materials. Despite the unprecedented availability of materials data in the scientific literature, much of this information remains trapped in unstructured figures and tables, hindering the construction of large language model (LLM)-based AI agent for automated materials design. Here, we present the Descriptive Interpretation of Visual Expression (DIVE) multi-agent workflow, which systematically reads and organizes experimental data from graphical elements in scientific literatures. We focus on solid-state hydrogen storage materials-a class of materials central to future clean-energy technologies and demonstrate that DIVE markedly improves the accuracy and coverage of data extraction compared to the direct extraction by multimodal models, with gains of 10-15% over commercial models and over 30% relative to open-source models. Building on a curated database of over 30,000 entries from 4,000 publications, we establish a rapid inverse design workflow capable of identifying previously unreported hydrogen storage compositions in two minutes. The proposed AI workflow and agent design are broadly transferable across diverse materials, providing a paradigm for AI-driven materials discovery.

