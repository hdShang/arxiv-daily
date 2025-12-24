---
layout: default
title: "BadPromptFL: A Novel Backdoor Threat to Prompt-based Federated Learning in Multimodal Models"
---

# BadPromptFL: A Novel Backdoor Threat to Prompt-based Federated Learning in Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08040" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08040v3</a>
  <a href="https://arxiv.org/pdf/2508.08040.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08040v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08040v3', 'BadPromptFL: A Novel Backdoor Threat to Prompt-based Federated Learning in Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maozhen Zhang, Mengnan Zhao, Wei Wang, Bo Wang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-11 (更新: 2025-09-06)

---

## 💡 一句话要点

**提出BadPromptFL以解决多模态模型中的后门攻击问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `后门攻击` `联邦学习` `多模态模型` `提示调优` `安全性` `CLIP架构` `攻击方法`

## 📋 核心要点

1. 现有的基于提示的联邦学习方法在安全性方面存在显著不足，尤其是对后门攻击的防御能力薄弱。
2. 论文提出BadPromptFL，通过优化本地后门触发器和提示嵌入，向全局聚合过程注入污染提示，形成新的攻击方式。
3. 实验结果显示，BadPromptFL在多个数据集上实现了超过90%的攻击成功率，且攻击隐蔽性强，客户端参与度低。

## 📝 摘要（中文）

基于提示的调优已成为大型视觉-语言模型中一种轻量级的替代方案，能够通过学习的上下文提示实现高效适应。最近，这一范式被扩展到联邦学习环境（如PromptFL），客户端在数据隐私约束下协作训练提示。然而，基于提示的聚合在联邦多模态学习中的安全性问题尚未得到充分探讨，留下了一个关键的攻击面。本文提出了BadPromptFL，这是首个针对多模态对比模型中基于提示的联邦学习的后门攻击。在BadPromptFL中，受损客户端共同优化本地后门触发器和提示嵌入，将污染的提示注入到全局聚合过程中。这些提示随后传播到良性客户端，使得在推理时无需修改模型参数即可实现通用后门激活。利用CLIP风格架构的上下文学习行为，BadPromptFL以极小的可见性和有限的客户端参与实现了高达90%以上的攻击成功率。对多个数据集和聚合协议的广泛实验验证了我们攻击的有效性、隐蔽性和普适性，提出了对基于提示的联邦学习在实际部署中鲁棒性的重大担忧。

## 🔬 方法详解

**问题定义**：本文旨在解决基于提示的联邦学习在多模态模型中面临的后门攻击问题。现有方法未能有效应对这一安全威胁，导致潜在的攻击面未被充分探讨。

**核心思路**：BadPromptFL的核心思路是通过受损客户端共同优化后门触发器和提示嵌入，向全局聚合过程注入污染提示，从而实现对良性客户端的攻击。这样的设计使得攻击者能够在不修改模型参数的情况下激活后门。

**技术框架**：BadPromptFL的整体架构包括多个阶段：首先，受损客户端生成本地后门触发器和提示嵌入；其次，这些污染提示被注入到全局模型中；最后，良性客户端接收到的提示在推理时触发后门。

**关键创新**：该研究的主要创新在于首次提出了针对多模态对比模型的后门攻击方法，利用了提示的上下文学习特性，使得攻击成功率高且隐蔽性强。

**关键设计**：在设计中，论文详细描述了后门触发器的生成过程、提示嵌入的优化策略，以及如何在不同聚合协议下保持攻击的有效性和隐蔽性。

## 📊 实验亮点

实验结果表明，BadPromptFL在多个数据集上实现了超过90%的攻击成功率，且在隐蔽性和客户端参与度方面表现优异。这一结果显著高于现有的防御机制，突显了该攻击方法的有效性和普适性。

## 🎯 应用场景

该研究的潜在应用场景包括安全敏感的多模态学习系统，如医疗影像分析、自动驾驶等领域。通过识别和防范后门攻击，可以提高这些系统的安全性和可靠性，确保在实际应用中不被恶意攻击所影响。

## 📄 摘要（原文）

> Prompt-based tuning has emerged as a lightweight alternative to full fine-tuning in large vision-language models, enabling efficient adaptation via learned contextual prompts. This paradigm has recently been extended to federated learning settings (e.g., PromptFL), where clients collaboratively train prompts under data privacy constraints. However, the security implications of prompt-based aggregation in federated multimodal learning remain largely unexplored, leaving a critical attack surface unaddressed. In this paper, we introduce \textbf{BadPromptFL}, the first backdoor attack targeting prompt-based federated learning in multimodal contrastive models. In BadPromptFL, compromised clients jointly optimize local backdoor triggers and prompt embeddings, injecting poisoned prompts into the global aggregation process. These prompts are then propagated to benign clients, enabling universal backdoor activation at inference without modifying model parameters. Leveraging the contextual learning behavior of CLIP-style architectures, BadPromptFL achieves high attack success rates (e.g., \(>90\%\)) with minimal visibility and limited client participation. Extensive experiments across multiple datasets and aggregation protocols validate the effectiveness, stealth, and generalizability of our attack, raising critical concerns about the robustness of prompt-based federated learning in real-world deployments.

