---
layout: default
title: SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents
---

# SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.10073" target="_blank" class="toolbar-btn">arXiv: 2510.10073v1</a>
    <a href="https://arxiv.org/pdf/2510.10073.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10073v1" 
            onclick="toggleFavorite(this, '2510.10073v1', 'SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zonghao Ying, Yangguang Shao, Jianle Gan, Gan Xu, Junjie Shen, Wenxin Zhang, Quanchen Zou, Junzheng Shi, Zhenfei Yin, Mingchuan Zhang, Aishan Liu, Xianglong Liu

**分类**: cs.CR, cs.CV

**发布日期**: 2025-10-11

---

## 💡 一句话要点

**SecureWebArena：LVLM Web Agent安全评估的综合基准**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `Web Agent` `安全评估` `大型视觉语言模型` `对抗性攻击` `基准测试`

## 📋 核心要点

1. 现有Web Agent安全评估基准覆盖范围有限，无法全面捕捉Agent的各种漏洞。
2. SecureWebArena通过构建包含多种攻击向量和Web环境的综合评估基准，实现对Agent安全性的全面评估。
3. 实验结果表明，现有LVLM Web Agent容易受到对抗性攻击，且模型专业化与安全性之间存在权衡。

## 📝 摘要（中文）

基于大型视觉语言模型（LVLM）的Web Agent正在成为自动化复杂在线任务的强大工具。然而，当部署在真实环境中时，它们面临着严重的安全风险，这促使人们设计安全评估基准。现有的基准仅提供部分覆盖，通常仅限于用户级别的提示操纵等狭窄场景，因此无法捕捉到广泛的Agent漏洞。为了解决这一差距，我们提出了SecureWebArena，这是第一个用于评估基于LVLM的Web Agent安全性的综合基准。SecureWebArena首先引入了一个统一的评估套件，包括六个模拟但真实的Web环境（例如，电子商务平台、社区论坛），并包含2970个高质量的轨迹，涵盖不同的任务和攻击设置。该套件定义了一个结构化的六种攻击向量分类，涵盖用户级别和环境级别的操纵。此外，我们引入了一个多层评估协议，分析Agent在三个关键维度上的失败：内部推理、行为轨迹和任务结果，从而促进了超越简单成功指标的细粒度风险分析。使用此基准，我们对9个具有代表性的LVLM进行了大规模实验，这些LVLM分为三类：通用型、Agent专用型和GUI-grounded型。我们的结果表明，所有测试的Agent都容易受到细微的对抗性操纵，并揭示了模型专业化和安全性之间的关键权衡。通过提供（1）具有多样化环境和多层评估管道的综合基准套件，以及（2）对现代基于LVLM的Web Agent的安全挑战的经验性见解，SecureWebArena为推进可信Web Agent的部署奠定了基础。

## 🔬 方法详解

**问题定义**：现有基于LVLM的Web Agent在真实环境中面临严重的安全风险，但现有的安全评估基准覆盖范围有限，无法全面评估Agent的安全性，尤其是在用户级别和环境级别的操纵方面。现有方法缺乏对Agent内部推理、行为轨迹和任务结果等多维度的细粒度分析。

**核心思路**：SecureWebArena的核心思路是构建一个综合性的安全评估基准，该基准包含多样化的Web环境、攻击向量和评估指标，从而能够全面评估LVLM Web Agent的安全性。通过模拟真实世界的攻击场景，并从多个维度分析Agent的失败原因，可以更准确地识别Agent的潜在漏洞。

**技术框架**：SecureWebArena包含以下主要组成部分：1) 六个模拟的Web环境，例如电子商务平台和社区论坛；2) 包含2970个高质量轨迹的数据集，涵盖不同的任务和攻击设置；3) 六种攻击向量的分类，涵盖用户级别和环境级别的操纵；4) 多层评估协议，分析Agent在内部推理、行为轨迹和任务结果三个维度上的失败。整体流程包括：Agent在模拟环境中执行任务，攻击者利用不同的攻击向量进行攻击，然后使用多层评估协议分析Agent的安全性。

**关键创新**：SecureWebArena的关键创新在于其综合性和多维度评估方法。与现有基准相比，SecureWebArena提供了更广泛的Web环境和攻击向量，能够更全面地评估Agent的安全性。此外，多层评估协议能够从内部推理、行为轨迹和任务结果等多个维度分析Agent的失败原因，从而提供更细粒度的风险分析。

**关键设计**：SecureWebArena的关键设计包括：1) Web环境的模拟，需要保证环境的真实性和多样性；2) 攻击向量的设计，需要涵盖用户级别和环境级别的各种操纵方式；3) 多层评估协议的设计，需要选择合适的评估指标来衡量Agent在不同维度上的表现。具体的参数设置、损失函数和网络结构等技术细节取决于所评估的LVLM Web Agent。

## 📊 实验亮点

通过在SecureWebArena上对9个代表性LVLM进行大规模实验，结果表明所有测试的Agent都容易受到细微的对抗性操纵。实验还揭示了模型专业化和安全性之间的关键权衡，即专门为Agent设计的模型可能在某些任务上表现更好，但同时也可能更容易受到攻击。

## 🎯 应用场景

该研究成果可应用于评估和提升各种基于LVLM的Web Agent的安全性，例如智能客服、自动化交易系统和内容审核工具。通过使用SecureWebArena进行安全评估，可以帮助开发者识别和修复Agent的潜在漏洞，从而提高Agent的可靠性和安全性，促进其在真实世界中的广泛应用。

## 📄 摘要（原文）

> Large vision-language model (LVLM)-based web agents are emerging as powerful tools for automating complex online tasks. However, when deployed in real-world environments, they face serious security risks, motivating the design of security evaluation benchmarks. Existing benchmarks provide only partial coverage, typically restricted to narrow scenarios such as user-level prompt manipulation, and thus fail to capture the broad range of agent vulnerabilities. To address this gap, we present \tool{}, the first holistic benchmark for evaluating the security of LVLM-based web agents. \tool{} first introduces a unified evaluation suite comprising six simulated but realistic web environments (\eg, e-commerce platforms, community forums) and includes 2,970 high-quality trajectories spanning diverse tasks and attack settings. The suite defines a structured taxonomy of six attack vectors spanning both user-level and environment-level manipulations. In addition, we introduce a multi-layered evaluation protocol that analyzes agent failures across three critical dimensions: internal reasoning, behavioral trajectory, and task outcome, facilitating a fine-grained risk analysis that goes far beyond simple success metrics. Using this benchmark, we conduct large-scale experiments on 9 representative LVLMs, which fall into three categories: general-purpose, agent-specialized, and GUI-grounded. Our results show that all tested agents are consistently vulnerable to subtle adversarial manipulations and reveal critical trade-offs between model specialization and security. By providing (1) a comprehensive benchmark suite with diverse environments and a multi-layered evaluation pipeline, and (2) empirical insights into the security challenges of modern LVLM-based web agents, \tool{} establishes a foundation for advancing trustworthy web agent deployment.

