---
layout: default
title: "Tenma: Robust Cross-Embodiment Robot Manipulation with Diffusion Transformer"
---

# Tenma: Robust Cross-Embodiment Robot Manipulation with Diffusion Transformer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.11865" class="toolbar-btn" target="_blank">📄 arXiv: 2509.11865v1</a>
  <a href="https://arxiv.org/pdf/2509.11865.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.11865v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.11865v1', 'Tenma: Robust Cross-Embodiment Robot Manipulation with Diffusion Transformer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Travis Davies, Yiqi Huang, Yunxin Liu, Xiang Chen, Huxian Liu, Luhui Hu

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-15

**备注**: 8 pages, 4 figures

---

## 💡 一句话要点

**提出Tenma以解决跨体态机器人操控的稳定性与性能问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `跨体态学习` `机器人操控` `多模态融合` `扩散模型` `Transformer` `双臂控制` `学习稳定性` `泛化能力`

## 📋 核心要点

1. 现有的机器人操控方法在跨体态学习中面临稳定性和性能不足的挑战，尤其是在多模态数据的处理上。
2. Tenma通过引入跨体态归一化器和联合状态-时间编码器，优化了扩散动作解码器，旨在提升双臂控制的稳定性和学习能力。
3. 实验结果显示，Tenma在匹配计算条件下的成功率达到88.95%，远超基线策略的18.12%，展现出强大的操控能力和泛化能力。

## 📝 摘要（中文）

随着Transformer策略和扩散模型的发展，机器人操控的能力得到了提升。然而，在轻量级的跨体态学习环境中，结合这些技术仍然面临挑战。本文研究了影响扩散-Transformer策略在异构多模态机器人数据上稳定性和性能的设计选择，提出了Tenma，一个用于双臂控制的轻量级扩散-Transformer。Tenma通过跨体态归一化器将不同的状态/动作空间映射到共享的潜在空间，采用联合状态-时间编码器进行时间对齐的观察学习，并优化了扩散动作解码器以提高训练稳定性和学习能力。在基准测试中，Tenma在匹配计算条件下实现了88.95%的平均成功率，显著超越了基线策略的18.12%。尽管使用了适中的数据规模，Tenma展现了强大的操控和泛化能力，表明多模态和跨体态学习策略在增强基于Transformer的模仿学习政策能力方面具有巨大潜力。

## 🔬 方法详解

**问题定义**：本论文旨在解决跨体态机器人操控中的稳定性和性能问题，现有方法在处理异构多模态数据时表现不佳，难以实现有效的学习和控制。

**核心思路**：Tenma的核心思路是通过跨体态归一化器将不同的状态和动作空间映射到一个共享的潜在空间，从而实现多模态数据的有效融合，并通过联合状态-时间编码器提升观察学习的时间对齐能力。

**技术框架**：Tenma的整体架构包括三个主要模块：跨体态归一化器、联合状态-时间编码器和扩散动作解码器。跨体态归一化器负责将异构数据映射到共享潜在空间，联合状态-时间编码器用于时间对齐的观察学习，而扩散动作解码器则优化了训练的稳定性和学习能力。

**关键创新**：Tenma的关键创新在于其轻量级设计和多模态融合能力，尤其是通过跨体态归一化器和联合状态-时间编码器的结合，使得在异构数据上实现了更高的学习效率和稳定性，这与现有方法的设计思路有显著区别。

**关键设计**：在设计中，Tenma采用了特定的损失函数以优化训练过程，并在网络结构上进行了精细调整，以确保在适中的数据规模下仍能实现高效的学习和泛化能力。具体的参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

Tenma在基准测试中表现出色，成功率达到88.95%，显著高于基线策略的18.12%。这一结果表明，Tenma在处理异构多模态数据时具备优越的稳定性和学习能力，展示了其在实际应用中的巨大潜力。

## 🎯 应用场景

Tenma的研究成果在多种机器人操控场景中具有广泛的应用潜力，尤其是在需要跨体态操作的复杂环境中，如服务机器人、工业自动化和人机协作等领域。其强大的泛化能力和稳定性将推动机器人技术的进一步发展，提升机器人在动态和多变环境中的适应能力。

## 📄 摘要（原文）

> Scaling Transformer policies and diffusion models has advanced robotic manipulation, yet combining these techniques in lightweight, cross-embodiment learning settings remains challenging. We study design choices that most affect stability and performance for diffusion-transformer policies trained on heterogeneous, multimodal robot data, and introduce Tenma, a lightweight diffusion-transformer for bi-manual arm control. Tenma integrates multiview RGB, proprioception, and language via a cross-embodiment normalizer that maps disparate state/action spaces into a shared latent space; a Joint State-Time encoder for temporally aligned observation learning with inference speed boosts; and a diffusion action decoder optimized for training stability and learning capacity. Across benchmarks and under matched compute, Tenma achieves an average success rate of 88.95% in-distribution and maintains strong performance under object and scene shifts, substantially exceeding baseline policies whose best in-distribution average is 18.12%. Despite using moderate data scale, Tenma delivers robust manipulation and generalization, indicating the great potential for multimodal and cross-embodiment learning strategies for further augmenting the capacity of transformer-based imitation learning policies.

