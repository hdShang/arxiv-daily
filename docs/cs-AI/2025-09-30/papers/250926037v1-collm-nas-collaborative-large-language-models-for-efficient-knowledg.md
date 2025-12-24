---
layout: default
title: "CoLLM-NAS: Collaborative Large Language Models for Efficient Knowledge-Guided Neural Architecture Search"
---

# CoLLM-NAS: Collaborative Large Language Models for Efficient Knowledge-Guided Neural Architecture Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26037" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26037v1</a>
  <a href="https://arxiv.org/pdf/2509.26037.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26037v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26037v1', 'CoLLM-NAS: Collaborative Large Language Models for Efficient Knowledge-Guided Neural Architecture Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhe Li, Zhiwei Lin, Yongtao Wang

**分类**: cs.AI, cs.CV, cs.LG

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出CoLLM-NAS，利用协同大语言模型进行高效的知识引导神经架构搜索**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `神经架构搜索` `大语言模型` `自动化机器学习` `知识引导` `协同学习`

## 📋 核心要点

1. 现有基于LLM的NAS方法存在架构无效、计算低效和性能不足等问题，限制了其应用。
2. CoLLM-NAS利用导航LLM指导搜索方向，生成器LLM合成高质量候选架构，并由协调器模块管理交互。
3. 实验表明，CoLLM-NAS在ImageNet和NAS-Bench-201上超越现有方法，并在多种搜索空间中提升了性能和效率。

## 📝 摘要（中文）

本文提出了一种基于协同大语言模型（LLM）的神经架构搜索（NAS）框架CoLLM-NAS，旨在解决现有方法中存在的架构无效性、计算效率低下以及性能不如传统NAS等问题。CoLLM-NAS是一个两阶段的NAS框架，通过两个互补的LLM进行知识引导搜索。具体来说，提出了一个导航LLM来指导搜索方向，以及一个生成器LLM来合成高质量的候选架构，并使用一个专门的协调器模块来管理它们的交互。CoLLM-NAS通过结合LLM固有的结构化神经架构知识以及来自迭代反馈和历史轨迹的渐进知识，有效地指导搜索过程。在ImageNet和NAS-Bench-201上的实验结果表明，CoLLM-NAS超越了现有的NAS方法和传统搜索算法，取得了新的state-of-the-art结果。此外，CoLLM-NAS持续提升了各种两阶段NAS方法（例如，OFA、SPOS和AutoFormer）在不同搜索空间（例如，MobileNet、ShuffleNet和AutoFormer）上的性能和效率，展示了其出色的泛化能力。

## 🔬 方法详解

**问题定义**：现有的基于大语言模型（LLM）的神经架构搜索（NAS）方法，虽然利用了LLM的知识，但常常生成无效的架构，计算效率低下，并且最终性能不如传统的NAS方法。这些问题阻碍了LLM在NAS领域的有效应用。

**核心思路**：CoLLM-NAS的核心思路是利用两个互补的LLM，一个负责导航搜索方向（Navigator LLM），另一个负责生成高质量的候选架构（Generator LLM），并通过一个协调器模块（Coordinator）来管理它们的交互。这种协同的方式旨在结合LLM的知识和迭代反馈，从而更有效地指导搜索过程。

**技术框架**：CoLLM-NAS是一个两阶段的NAS框架。第一阶段，Navigator LLM根据历史搜索轨迹和反馈，指导Generator LLM生成候选架构。第二阶段，Coordinator模块评估这些候选架构，并将结果反馈给Navigator LLM，用于下一轮的搜索指导。这个过程迭代进行，直到找到最优架构。

**关键创新**：CoLLM-NAS的关键创新在于协同使用两个LLM，并引入协调器模块来管理它们的交互。Navigator LLM利用历史信息和反馈来指导搜索方向，Generator LLM则专注于生成高质量的候选架构。这种分工合作的方式能够更有效地利用LLM的知识，并避免生成无效或低效的架构。

**关键设计**：Navigator LLM和Generator LLM的具体选择和训练方式未知，Coordinator模块的评估策略也未知。论文中可能使用了特定的prompt工程技术来引导LLM的行为。损失函数的设计可能包括对架构有效性和性能的约束。具体的网络结构细节取决于所搜索的空间（例如，MobileNet、ShuffleNet、AutoFormer）。

## 📊 实验亮点

CoLLM-NAS在ImageNet和NAS-Bench-201上取得了state-of-the-art的结果，超越了现有的NAS方法和传统搜索算法。此外，CoLLM-NAS能够持续提升各种两阶段NAS方法（例如，OFA、SPOS和AutoFormer）在不同搜索空间（例如，MobileNet、ShuffleNet和AutoFormer）上的性能和效率，展示了其出色的泛化能力。具体的性能提升幅度未知。

## 🎯 应用场景

CoLLM-NAS具有广泛的应用前景，可用于自动化设计各种神经网络架构，例如图像分类、目标检测、自然语言处理等领域的模型。该方法能够降低模型设计的门槛，加速新模型的开发，并提高模型性能。未来，CoLLM-NAS有望应用于更复杂的任务和更大的搜索空间，推动人工智能技术的发展。

## 📄 摘要（原文）

> The integration of Large Language Models (LLMs) with Neural Architecture Search (NAS) has introduced new possibilities for automating the design of neural architectures. However, most existing methods face critical limitations, including architectural invalidity, computational inefficiency, and inferior performance compared to traditional NAS. In this work, we present Collaborative LLM-based NAS (CoLLM-NAS), a two-stage NAS framework with knowledge-guided search driven by two complementary LLMs. Specifically, we propose a Navigator LLM to guide search direction and a Generator LLM to synthesize high-quality candidates, with a dedicated Coordinator module to manage their interaction. CoLLM-NAS efficiently guides the search process by combining LLMs' inherent knowledge of structured neural architectures with progressive knowledge from iterative feedback and historical trajectory. Experimental results on ImageNet and NAS-Bench-201 show that CoLLM-NAS surpasses existing NAS methods and conventional search algorithms, achieving new state-of-the-art results. Furthermore, CoLLM-NAS consistently enhances the performance and efficiency of various two-stage NAS methods (e.g., OFA, SPOS, and AutoFormer) across diverse search spaces (e.g., MobileNet, ShuffleNet, and AutoFormer), demonstrating its excellent generalization.

