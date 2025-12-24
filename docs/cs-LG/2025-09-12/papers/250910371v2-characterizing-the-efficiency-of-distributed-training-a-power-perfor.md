---
layout: default
title: "Characterizing the Efficiency of Distributed Training: A Power, Performance, and Thermal Perspective"
---

# Characterizing the Efficiency of Distributed Training: A Power, Performance, and Thermal Perspective

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10371" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10371v2</a>
  <a href="https://arxiv.org/pdf/2509.10371.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10371v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10371v2', 'Characterizing the Efficiency of Distributed Training: A Power, Performance, and Thermal Perspective')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seokjin Go, Joongun Park, Spandan More, Hanjiang Wu, Irene Wang, Aaron Jezghani, Tushar Krishna, Divya Mahajan

**分类**: cs.DC, cs.LG

**发布日期**: 2025-09-12 (更新: 2025-09-19)

**🔗 代码/项目**: [GITHUB](https://github.com/sitar-lab/CharLLM-PPT)

---

## 💡 一句话要点

**深入剖析LLM分布式训练效率：从功耗、性能和热管理的角度进行全面评估**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `分布式训练` `大规模语言模型` `性能分析` `功耗分析` `热管理` `并行策略` `硬件平台`

## 📋 核心要点

1. 现有LLM训练对单节点分析提出挑战，需要深入理解模型在多GPU系统中的行为。
2. 通过分析不同并行策略对硬件利用率、功耗和热行为的影响，揭示训练性能与硬件、系统和模型执行的复杂关系。
3. 研究结果为系统和硬件设计提供了建议，旨在提升未来LLM系统和工作负载的可扩展性和可靠性。

## 📝 摘要（中文）

本文针对大规模语言模型（LLM）的训练，在包括NVIDIA H100/H200和AMD MI250 GPU在内的多种真实硬件平台上，进行了全面的性能分析。研究涵盖了稠密和稀疏模型，以及张量并行、流水线并行、数据并行和专家并行等多种并行策略，并评估了它们对硬件利用率、功耗和热行为的影响。此外，还评估了激活重计算和计算-通信重叠等优化技术的有效性。研究表明，性能并非完全由硬件容量决定。在通信受限的情况下，采用少量高内存GPU的纵向扩展系统可能优于横向扩展系统，但需要仔细调整配置；在其他情况下，横向扩展部署可实现更高的吞吐量。某些并行组合（如张量并行与流水线并行）会导致带宽利用率不足，而增加微批大小超过一定程度会导致突发执行和峰值功率偏移，从而加剧热节流。这些发现揭示了训练性能如何受到硬件、系统拓扑和模型执行之间复杂交互的影响。最后，为改进未来LLM系统和工作负载的可扩展性和可靠性，提出了系统和硬件设计的建议。项目源代码可在https://github.com/sitar-lab/CharLLM-PPT获取。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模语言模型（LLM）在分布式训练过程中，硬件资源利用率、功耗、热管理以及不同并行策略选择等问题。现有方法难以充分理解硬件、系统拓扑和模型执行之间的复杂交互，导致训练效率低下，难以优化系统设计。

**核心思路**：论文的核心思路是通过对LLM训练过程进行全面的性能剖析，深入理解不同并行策略、硬件平台和优化技术对硬件利用率、功耗和热行为的影响。通过实验数据和分析，揭示影响训练效率的关键因素，并为系统和硬件设计提供指导。

**技术框架**：论文的技术框架主要包括以下几个阶段：1) 选择具有代表性的LLM模型和数据集；2) 在不同的硬件平台（如NVIDIA H100/H200和AMD MI250 GPU）上进行训练；3) 采用不同的并行策略（如张量并行、流水线并行、数据并行和专家并行）；4) 评估硬件利用率、功耗和热行为；5) 分析实验数据，找出影响训练效率的关键因素；6) 提出系统和硬件设计的建议。

**关键创新**：论文的关键创新在于对LLM分布式训练过程进行了全面的性能剖析，并揭示了硬件、系统拓扑和模型执行之间复杂的交互关系。与现有方法相比，该研究不仅关注性能指标，还深入分析了功耗和热行为，从而更全面地理解了训练过程。此外，该研究还针对不同的并行策略和硬件平台进行了评估，为实际应用提供了更具体的指导。

**关键设计**：论文的关键设计包括：1) 选择具有代表性的LLM模型，如稠密和稀疏模型；2) 采用多种并行策略，如张量并行、流水线并行、数据并行和专家并行；3) 评估硬件利用率、功耗和热行为，包括GPU利用率、功耗、温度等指标；4) 分析实验数据，找出影响训练效率的关键因素，如通信瓶颈、内存限制等；5) 提出系统和硬件设计的建议，如优化数据chunking、调整微批大小等。

## 📊 实验亮点

研究表明，在通信受限的情况下，采用少量高内存GPU的纵向扩展系统可能优于横向扩展系统，但需要仔细调整配置。某些并行组合（如张量并行与流水线并行）会导致带宽利用率不足。增加微批大小超过一定程度会导致突发执行和峰值功率偏移，从而加剧热节流。这些发现强调了硬件、系统拓扑和模型执行之间复杂交互对训练性能的影响。

## 🎯 应用场景

该研究成果可应用于大规模语言模型的训练优化、高性能计算系统设计、以及AI芯片的研发。通过理解不同并行策略和硬件平台对训练效率的影响，可以指导用户选择合适的硬件配置和并行策略，从而降低训练成本、缩短训练时间，并提升AI模型的性能。此外，该研究还可以为未来的AI芯片设计提供参考，使其更适合LLM的训练。

## 📄 摘要（原文）

> The rapid scaling of Large Language Models (LLMs) has pushed training workloads far beyond the limits of single-node analysis, demanding a deeper understanding of how these models behave across large-scale, multi-GPU systems. In this paper, we present a comprehensive characterization of LLM training across diverse real-world workloads and hardware platforms, including NVIDIA H100/H200 and AMD MI250 GPUs. We analyze dense and sparse models under various parallelism strategies -- tensor, pipeline, data, and expert -- and evaluate their effects on hardware utilization, power consumption, and thermal behavior. We further evaluate the effectiveness of optimizations such as activation recomputation and compute-communication overlap. Our findings show that performance is not determined solely by scaling hardware capacity. Scale-up systems with fewer, higher-memory GPUs can outperform scale-out systems in communication-bound regimes, but only under carefully tuned configurations; in other cases, scale-out deployments achieve superior throughput. We also show that certain parallelism combinations, such as tensor with pipeline, lead to bandwidth underutilization due to inefficient data chunking, while increasing microbatch sizes beyond a certain point induces bursty execution and peak power excursions that worsen thermal throttling. These insights reveal how training performance is shaped by complex interactions between hardware, system topology, and model execution. We conclude by offering recommendations for system and hardware design to improve the scalability and reliability of future LLM systems and workloads. The source code of this project is available at https://github.com/sitar-lab/CharLLM-PPT.

