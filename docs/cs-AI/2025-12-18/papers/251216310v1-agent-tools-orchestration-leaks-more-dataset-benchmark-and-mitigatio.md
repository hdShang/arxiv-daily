---
layout: default
title: "Agent Tools Orchestration Leaks More: Dataset, Benchmark, and Mitigation"
---

# Agent Tools Orchestration Leaks More: Dataset, Benchmark, and Mitigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16310" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16310v1</a>
  <a href="https://arxiv.org/pdf/2512.16310.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16310v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16310v1', 'Agent Tools Orchestration Leaks More: Dataset, Benchmark, and Mitigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxuan Qiao, Dongqin Liu, Hongchang Yang, Wei Zhou, Songlin Hu

**分类**: cs.CR, cs.AI, cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**揭示Agent工具编排中的隐私泄露风险，并提出TOP-Bench基准与PEP缓解方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Agent工具编排` `隐私泄露风险` `大型语言模型` `隐私增强原则` `基准测试` `目标函数对齐` `安全与鲁棒性权衡`

## 📋 核心要点

1. 现有Agent架构在追求有用性的同时，忽略了隐私保护，导致工具编排过程中存在严重的隐私泄露风险。
2. 论文提出隐私增强原则(PEP)方法，通过调整Agent的目标函数，使其在追求有用性的同时兼顾隐私保护。
3. 实验结果表明，PEP方法能够有效降低风险泄露率，显著提高安全性和鲁棒性之间的权衡指标H-Score。

## 📝 摘要（中文）

本文系统性地研究了由大型语言模型驱动的单智能体多工具架构中存在的工具编排隐私风险(TOP-R)。这种架构为了实现用户目标，可能自主地聚合多个工具中的信息片段，并利用其推理能力合成意想不到的敏感信息。研究首先建立了一个形式化框架，将风险的根本原因归结为智能体目标函数的错位：过度优化了有用性而忽略了隐私意识。其次，构建了TOP-Bench，包含配对的泄露和良性场景，以全面评估这种风险。为了量化安全性和鲁棒性之间的权衡，引入了H-Score作为整体指标。评估结果表明TOP-R是一个严重的风险：八个代表性模型的平均风险泄露率(RLR)达到90.24%，而平均H-Score仅为0.167，没有模型超过0.3。最后，提出了隐私增强原则(PEP)方法，有效地缓解了TOP-R，将风险泄露率降低到46.58%，并将H-Score显著提高到0.624。这项工作揭示了一种新型风险以及当前智能体架构中固有的结构性限制，同时也提供了可行的缓解策略。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型驱动的Agent在工具编排过程中产生的隐私泄露问题（Tools Orchestration Privacy Risk, TOP-R）。现有Agent架构过度优化了有用性，忽略了隐私保护，导致Agent可能自主地聚合多个工具中的信息片段，并推理出敏感信息。现有方法缺乏对这种风险的系统性研究和有效的缓解策略。

**核心思路**：论文的核心思路是识别并缓解Agent目标函数中的错位，即过度强调有用性而忽略隐私意识。通过引入隐私增强原则(PEP)，调整Agent的目标函数，使其在追求有用性的同时，也考虑到隐私保护。这样可以避免Agent为了达成目标而过度利用工具，从而减少隐私泄露的风险。

**技术框架**：论文的技术框架主要包括三个部分：1) 形式化框架：用于定义和分析TOP-R的根本原因，将其归结为Agent目标函数的错位。2) TOP-Bench基准：包含配对的泄露和良性场景，用于评估Agent的隐私泄露风险。3) 隐私增强原则(PEP)方法：用于缓解TOP-R，通过调整Agent的目标函数，使其兼顾有用性和隐私保护。整体流程是先通过TOP-Bench评估现有Agent的隐私泄露风险，然后应用PEP方法进行缓解，最后再次通过TOP-Bench评估缓解效果。

**关键创新**：论文最重要的技术创新点在于提出了隐私增强原则(PEP)方法。与现有方法不同，PEP方法不是简单地限制Agent对工具的使用，而是通过调整Agent的目标函数，使其在追求有用性的同时，也考虑到隐私保护。这种方法更加灵活和有效，可以更好地平衡安全性和鲁棒性。此外，TOP-Bench基准的构建也为评估Agent的隐私泄露风险提供了一个标准化的平台。

**关键设计**：关于PEP方法的具体实现细节，论文中可能涉及对损失函数的修改，例如引入一个惩罚项，用于惩罚Agent的隐私泄露行为。具体参数设置和网络结构的选择可能取决于具体的Agent模型和任务。TOP-Bench基准的设计需要仔细考虑泄露场景和良性场景的构建，确保能够有效地评估Agent的隐私泄露风险。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16310v1/Problem_Introduction.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16310v1/Dataset_Construction.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16310v1/x1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，现有Agent模型存在严重的隐私泄露风险，平均风险泄露率(RLR)高达90.24%，平均H-Score仅为0.167。应用PEP方法后，风险泄露率显著降低到46.58%，H-Score显著提高到0.624。这表明PEP方法能够有效地缓解TOP-R，并在安全性和鲁棒性之间取得更好的平衡。

## 🎯 应用场景

该研究成果可应用于各种需要使用Agent进行自动化任务处理的领域，例如智能客服、自动化办公、智能家居等。通过降低Agent的隐私泄露风险，可以提高用户对Agent的信任度，促进Agent技术的广泛应用。未来，该研究可以进一步扩展到多Agent协作场景，研究更复杂的隐私泄露风险和缓解策略。

## 📄 摘要（原文）

> Driven by Large Language Models, the single-agent, multi-tool architecture has become a popular paradigm for autonomous agents due to its simplicity and effectiveness. However, this architecture also introduces a new and severe privacy risk, which we term Tools Orchestration Privacy Risk (TOP-R), where an agent, to achieve a benign user goal, autonomously aggregates information fragments across multiple tools and leverages its reasoning capabilities to synthesize unexpected sensitive information. We provide the first systematic study of this risk. First, we establish a formal framework, attributing the risk's root cause to the agent's misaligned objective function: an overoptimization for helpfulness while neglecting privacy awareness. Second, we construct TOP-Bench, comprising paired leakage and benign scenarios, to comprehensively evaluate this risk. To quantify the trade-off between safety and robustness, we introduce the H-Score as a holistic metric. The evaluation results reveal that TOP-R is a severe risk: the average Risk Leakage Rate (RLR) of eight representative models reaches 90.24%, while the average H-Score is merely 0.167, with no model exceeding 0.3. Finally, we propose the Privacy Enhancement Principle (PEP) method, which effectively mitigates TOP-R, reducing the Risk Leakage Rate to 46.58% and significantly improving the H-Score to 0.624. Our work reveals both a new class of risk and inherent structural limitations in current agent architectures, while also offering feasible mitigation strategies.

