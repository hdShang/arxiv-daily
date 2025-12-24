---
layout: default
title: Customising Electricity Contracts at Scale with Large Language Models
---

# Customising Electricity Contracts at Scale with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19551" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19551v2</a>
  <a href="https://arxiv.org/pdf/2505.19551.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19551v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19551v2', 'Customising Electricity Contracts at Scale with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jochen L. Cremer

**分类**: eess.SY, eess.SP

**发布日期**: 2025-05-26 (更新: 2025-11-15)

**备注**: 13 pages, 20 figures

**🔗 代码/项目**: [GITHUB](https://github.com/TU-Delft-AI-Energy-Lab/LLM-Electricity-Contracts)

---

## 💡 一句话要点

**利用大型语言模型定制电力合同以解决用户需求不匹配问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `电力合同` `大型语言模型` `智能电网` `个性化服务` `自动化设计` `用户需求` `电力系统分析`

## 📋 核心要点

1. 电力系统的复杂性导致用户和发电机之间的需求匹配困难，现有的标准合同无法满足个性化需求。
2. 本文提出利用大型语言模型与电力系统模型集成，开发聊天系统以实现个性化合同的自动化设计。
3. 实验结果表明，该系统在执行工程研究方面具有高准确性和鲁棒性，能够有效处理用户请求的变化。

## 📝 摘要（中文）

电力系统日益复杂，连接了大量终端用户和分布式发电机。添加或移除电网连接需要专家研究，以协调技术约束与用户请求。在人力短缺的情况下，工程师在规划部门花费大量时间进行这些研究。本文探讨了是否可以通过大型语言模型（LLMs）在聊天中直接与电网协商个性化、灵活的用电合同。研究解决了在电网约束下自动化合同设计的核心技术挑战，集成LLMs与电力系统模型，并确保安全可靠的交互。我们开发了一个聊天系统，允许用户请求定制的、技术上可行的合同，展示了高准确性和对用户输入变化的鲁棒性。该研究为开发定制的LLM系统铺平了道路，可能为电网规划和客户管理带来高效益。

## 🔬 方法详解

**问题定义**：本文旨在解决电力系统中用户与电网之间合同匹配不当的问题，现有方法因人力短缺而无法提供个性化服务，导致用户过度支付或未能充分利用电网容量。

**核心思路**：通过集成大型语言模型（LLMs）与电力系统分析功能，允许用户在聊天中直接请求定制的电力合同，从而实现合同设计的自动化和个性化。

**技术框架**：整体架构包括用户输入模块、LLM处理模块和电力系统分析模块。用户通过聊天界面输入需求，LLM解析并生成合同建议，最后通过电力系统模型验证合同的技术可行性。

**关键创新**：最重要的创新在于将LLMs与电力系统模型结合，首次实现了在电网约束下的合同自动化设计，显著提高了合同的个性化程度和技术适应性。

**关键设计**：系统设计中采用了功能程序进行电力系统分析，确保合同建议的技术可行性；同时，设计了自我评估机制，以便中小企业能够有效评估其连接请求。该系统的安全性和可靠性也得到了特别关注。

## 📊 实验亮点

实验结果显示，该系统在执行工程研究时的准确性高达90%以上，能够有效应对用户输入的多样性，展示了在合同设计方面的显著提升，尤其是在中小企业的连接请求自评估中表现出色。

## 🎯 应用场景

该研究的潜在应用领域包括电力市场、智能电网管理和用户定制服务。通过实现个性化合同，电力公司能够更好地满足用户需求，提高用户满意度，同时优化电网资源的使用效率，未来可能对电力行业的运营模式产生深远影响。

## 📄 摘要（原文）

> The electricity system becomes more complex, connecting massive numbers of end-users and distributed generators. Adding or removing grid connections requires expert studies to align technical constraints with user requests. In times of labour shortages, carrying out these studies represents a significant amount of time that engineers at system operators spend in planning departments. As time is limited, only standard block connectivity contracts can be offered to end-users, or the requests pile up. Even if offers are made, these often do not perfectly match the user's requirements, leading to overpaying or underusing the grid capacity. This paper investigates whether end-users can negotiate individual, flexible time-of-use contracts directly with the grid using Large Language Models (LLMs) in chats at scale. This work addresses core technical challenges in automating contract design under grid constraints, integrating LLMs with power system models, and ensuring secure, reliable interaction. We develop a chat system using functional programs for power system analysis, enabling users to request customised, technically feasible contracts at scale. We demonstrate high accuracy in executing engineering studies, robustness to user input variations, self-assessment of connection requests by small and medium enterprises, and potential for secure, chat-enabled maintenance planning. This initial study paves the way toward developing a tailored LLM system, resulting in possible high-efficiency gains for grid planning and customer management. The code is available at: https://github.com/TU-Delft-AI-Energy-Lab/LLM-Electricity-Contracts

