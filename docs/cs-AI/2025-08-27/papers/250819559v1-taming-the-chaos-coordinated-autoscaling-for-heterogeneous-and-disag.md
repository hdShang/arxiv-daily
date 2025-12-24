---
layout: default
title: "Taming the Chaos: Coordinated Autoscaling for Heterogeneous and Disaggregated LLM Inference"
---

# Taming the Chaos: Coordinated Autoscaling for Heterogeneous and Disaggregated LLM Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19559" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19559v1</a>
  <a href="https://arxiv.org/pdf/2508.19559.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19559v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19559v1', 'Taming the Chaos: Coordinated Autoscaling for Heterogeneous and Disaggregated LLM Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rongzhi Li, Ruogu Du, Zefang Chu, Sida Zhao, Chunlei Han, Zuocheng Shi, Yiwen Shao, Huanle Han, Long Huang, Zherui Liu, Shufan Liu

**分类**: cs.DC, cs.AI

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出HeteroScale以解决异构和分离LLM推理的自动扩展问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `自动扩展` `异构计算` `资源管理` `Prefill-Decode架构`

## 📋 核心要点

1. 现有的自动扩展方法在处理现代分离架构时面临异构硬件利用不均、网络瓶颈及预填充与解码阶段不平衡等挑战。
2. HeteroScale框架通过拓扑感知调度器和基于度量的策略，协调扩展预填充和解码池，优化资源管理。
3. 在大规模生产环境中，HeteroScale显著提高了GPU利用率26.6个百分点，节省了大量GPU小时，确保了服务质量。

## 📝 摘要（中文）

大型语言模型（LLMs）的服务是一项GPU密集型任务，传统的自动扩展方法在现代的Prefill-Decode（P/D）分离架构中表现不佳。此架构转变虽然强大，但带来了显著的操作挑战，包括异构硬件的低效利用、网络瓶颈以及预填充和解码阶段之间的关键不平衡。我们提出了HeteroScale，一个协调的自动扩展框架，旨在解决P/D分离服务的核心挑战。HeteroScale结合了一个拓扑感知调度器，能够适应异构硬件和网络约束，以及一种基于大规模实证研究的创新度量驱动策略。通过利用单一的强健度量来共同扩展预填充和解码池，HeteroScale保持了架构平衡，同时确保了高效的自适应资源管理。在数万GPU的大规模生产环境中部署后，HeteroScale证明了其有效性，平均GPU利用率提高了26.6个百分点，每日节省数十万GPU小时，同时保持严格的服务水平目标。

## 🔬 方法详解

**问题定义**：本论文旨在解决在现代Prefill-Decode（P/D）分离架构中，传统自动扩展方法在异构硬件利用、网络瓶颈及阶段不平衡等方面的不足。

**核心思路**：HeteroScale通过结合拓扑感知调度器和度量驱动策略，协调扩展预填充和解码资源，以实现高效的资源管理和架构平衡。

**技术框架**：HeteroScale的整体架构包括拓扑感知调度器、度量驱动策略和资源管理模块，能够根据硬件和网络条件动态调整资源分配。

**关键创新**：HeteroScale的主要创新在于其基于大规模实证研究的度量驱动策略，能够有效地协调异构资源的使用，解决传统方法的局限性。

**关键设计**：在设计中，HeteroScale使用了单一的强健度量来共同扩展预填充和解码池，确保了资源的高效利用和服务质量的稳定性。

## 📊 实验亮点

HeteroScale在大规模生产环境中表现出色，平均GPU利用率提高了26.6个百分点，显著节省了数十万GPU小时，且在保持严格服务水平目标的同时，优化了资源管理。这些结果表明HeteroScale在实际应用中的有效性和重要性。

## 🎯 应用场景

HeteroScale的研究成果在大型语言模型的服务领域具有广泛的应用潜力，尤其是在需要高效资源管理和实时响应的场景中，如在线客服、智能助手和内容生成等。其创新的自动扩展方法可以显著提升系统的性能和用户体验，未来可能推动更多智能应用的发展。

## 📄 摘要（原文）

> Serving Large Language Models (LLMs) is a GPU-intensive task where traditional autoscalers fall short, particularly for modern Prefill-Decode (P/D) disaggregated architectures. This architectural shift, while powerful, introduces significant operational challenges, including inefficient use of heterogeneous hardware, network bottlenecks, and critical imbalances between prefill and decode stages. We introduce HeteroScale, a coordinated autoscaling framework that addresses the core challenges of P/D disaggregated serving. HeteroScale combines a topology-aware scheduler that adapts to heterogeneous hardware and network constraints with a novel metric-driven policy derived from the first large-scale empirical study of autoscaling signals in production. By leveraging a single, robust metric to jointly scale prefill and decode pools, HeteroScale maintains architectural balance while ensuring efficient, adaptive resource management. Deployed in a massive production environment on tens of thousands of GPUs, HeteroScale has proven its effectiveness, increasing average GPU utilization by a significant 26.6 percentage points and saving hundreds of thousands of GPU-hours daily, all while upholding stringent service level objectives.

