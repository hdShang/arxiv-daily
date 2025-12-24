---
layout: default
title: "SanDRA: Safe Large-Language-Model-Based Decision Making for Automated Vehicles Using Reachability Analysis"
---

# SanDRA: Safe Large-Language-Model-Based Decision Making for Automated Vehicles Using Reachability Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.06717" class="toolbar-btn" target="_blank">📄 arXiv: 2510.06717v1</a>
  <a href="https://arxiv.org/pdf/2510.06717.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.06717v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.06717v1', 'SanDRA: Safe Large-Language-Model-Based Decision Making for Automated Vehicles Using Reachability Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuanfei Lin, Sebastian Illing, Matthias Althoff

**分类**: cs.RO

**发布日期**: 2025-10-08

**备注**: @2025 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works

---

## 💡 一句话要点

**SanDRA：基于可达性分析的自动驾驶车辆安全大语言模型决策框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `大语言模型` `可达性分析` `安全决策` `时序逻辑` `形式化验证` `交通规则`

## 📋 核心要点

1. 现有基于大语言模型的自动驾驶决策方法缺乏对车辆动力学的整合，且存在幻觉问题，导致决策安全性难以保证。
2. SanDRA框架利用可达性分析，对大语言模型生成的驾驶行为进行安全验证，从而消除不安全行为，确保决策安全性。
3. 实验结果表明，SanDRA框架即使在高密度交通条件下，也能提供安全且符合法律规定的驾驶行为，具有良好的应用前景。

## 📝 摘要（中文）

本文提出SanDRA，一种基于可达性分析的自动驾驶车辆安全大语言模型决策框架。该框架利用大语言模型强大的泛化和推理能力，为自动驾驶车辆提供知识驱动的决策。首先，通过对驾驶场景的全面描述，提示大语言模型生成并排序可行的驾驶行为。然后，将这些行为转化为包含形式化交通规则的时序逻辑公式，并将其整合到可达性分析中，以消除不安全的行为。通过在开放和闭环驾驶环境中，使用现成和微调的大语言模型验证了该方法，结果表明，即使在高密度交通条件下，该方法也能提供可证明安全且在可能情况下符合法律规定的驾驶行为。所有代码和实验设置均已公开。

## 🔬 方法详解

**问题定义**：自动驾驶车辆的决策系统需要具备安全性和合规性，而直接使用大语言模型进行决策可能由于其固有的不确定性和缺乏对车辆动力学的考虑，导致不安全的行为。现有方法难以保证决策的安全性，尤其是在复杂交通场景下。

**核心思路**：SanDRA的核心思路是将大语言模型的知识推理能力与可达性分析的安全验证能力相结合。首先利用大语言模型生成候选驾驶行为，然后通过可达性分析验证这些行为的安全性，从而确保最终决策的安全性和合规性。

**技术框架**：SanDRA框架包含以下主要模块：1) 场景描述模块：对驾驶场景进行全面描述，包括交通规则、车辆状态、周围环境等信息。2) 大语言模型决策模块：利用场景描述提示大语言模型生成并排序可行的驾驶行为。3) 时序逻辑公式转换模块：将驾驶行为转化为包含形式化交通规则的时序逻辑公式。4) 可达性分析模块：利用可达性分析验证驾驶行为的安全性，消除不安全行为。5) 决策执行模块：执行经过安全验证的驾驶行为。

**关键创新**：SanDRA的关键创新在于将大语言模型的决策能力与可达性分析的安全验证能力相结合，提出了一种安全的大语言模型驱动的自动驾驶决策框架。这是首次尝试将可达性分析应用于大语言模型驱动的自动驾驶决策中，有效解决了大语言模型决策安全性难以保证的问题。

**关键设计**：在场景描述模块中，需要设计合适的提示语，以引导大语言模型生成高质量的驾驶行为。在时序逻辑公式转换模块中，需要将交通规则进行形式化表示，并将其融入到时序逻辑公式中。在可达性分析模块中，需要选择合适的车辆动力学模型和可达集计算方法，以保证安全验证的准确性和效率。

## 📊 实验亮点

论文在开放和闭环驾驶环境中，使用现成和微调的大语言模型验证了SanDRA框架的有效性。实验结果表明，即使在高密度交通条件下，该框架也能提供可证明安全且在可能情况下符合法律规定的驾驶行为。代码和实验设置已公开，方便复现和进一步研究。

## 🎯 应用场景

SanDRA框架可应用于各种自动驾驶场景，例如城市道路、高速公路等。该框架能够提高自动驾驶车辆的安全性，降低事故风险，并有助于实现更高级别的自动驾驶。此外，该框架还可以用于自动驾驶车辆的测试和验证，以评估其安全性和合规性。

## 📄 摘要（原文）

> Large language models have been widely applied to knowledge-driven decision-making for automated vehicles due to their strong generalization and reasoning capabilities. However, the safety of the resulting decisions cannot be ensured due to possible hallucinations and the lack of integrated vehicle dynamics. To address this issue, we propose SanDRA, the first safe large-language-model-based decision making framework for automated vehicles using reachability analysis. Our approach starts with a comprehensive description of the driving scenario to prompt large language models to generate and rank feasible driving actions. These actions are translated into temporal logic formulas that incorporate formalized traffic rules, and are subsequently integrated into reachability analysis to eliminate unsafe actions. We validate our approach in both open-loop and closed-loop driving environments using off-the-shelf and finetuned large language models, showing that it can provide provably safe and, where possible, legally compliant driving actions, even under high-density traffic conditions. To ensure transparency and facilitate future research, all code and experimental setups are publicly available at github.com/CommonRoad/SanDRA.

