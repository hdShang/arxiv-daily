---
layout: default
title: SafeCoop: Unravelling Full Stack Safety in Agentic Collaborative Driving
---

# SafeCoop: Unravelling Full Stack Safety in Agentic Collaborative Driving

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.18123" target="_blank" class="toolbar-btn">arXiv: 2510.18123v1</a>
    <a href="https://arxiv.org/pdf/2510.18123.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.18123v1" 
            onclick="toggleFavorite(this, '2510.18123v1', 'SafeCoop: Unravelling Full Stack Safety in Agentic Collaborative Driving')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xiangbo Gao, Tzu-Hsiang Lin, Ruojing Song, Yuheng Wu, Kuan-Ru Huang, Zicheng Jin, Fangzhou Lin, Shinan Liu, Zhengzhong Tu

**分类**: cs.CV, cs.AI, cs.CL, cs.RO

**发布日期**: 2025-10-20

**🔗 代码/项目**: [PROJECT_PAGE](https://xiangbogaobarry.github.io/SafeCoop)

---

## 💡 一句话要点

**SafeCoop：针对基于自然语言协同驾驶的全栈安全防御框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `协同驾驶` `自然语言处理` `安全防御` `智能交通系统` `车联网安全`

## 📋 核心要点

1. 传统协同驾驶系统依赖高带宽的传感器数据通信，存在语义损失和互操作性问题，而基于自然语言的协同驾驶面临新的安全威胁。
2. SafeCoop提出了一种Agentic防御管道，通过语义防火墙、语言-感知一致性检查和多源共识来应对自然语言协同驾驶中的安全漏洞。
3. 实验结果表明，SafeCoop在恶意攻击下显著提升了驾驶评分和恶意检测的F1分数，验证了其有效性。

## 📝 摘要（中文）

协同驾驶系统利用车联网（V2X）通信来增强驾驶安全性和效率。传统的V2X系统以原始传感器数据、神经特征或感知结果作为通信媒介，面临着高带宽需求、语义损失和互操作性问题等挑战。最近的研究表明，自然语言作为一种有前景的媒介，能够以显著降低的带宽提供语义丰富性、决策层推理以及人机互操作性。然而，这种范式转变也带来了新的安全漏洞，包括消息丢失、幻觉、语义操纵和对抗性攻击。本文首次系统地研究了基于自然语言协同驾驶中的全栈安全问题。具体而言，我们开发了一个全面的攻击策略分类，包括连接中断、中继/重放干扰、内容欺骗和多连接伪造。为了缓解这些风险，我们引入了一个名为SafeCoop的Agentic防御管道，它集成了语义防火墙、语言-感知一致性检查和多源共识，并通过Agentic转换函数实现跨帧空间对齐。我们在CARLA闭环仿真中，针对32个关键场景系统地评估了SafeCoop，在恶意攻击下实现了69.15%的驾驶评分提升，恶意检测的F1分数高达67.32%。这项研究为推进交通系统中安全、可靠和值得信赖的语言驱动协作研究提供了指导。

## 🔬 方法详解

**问题定义**：论文旨在解决基于自然语言的协同驾驶系统中存在的安全漏洞问题。现有方法主要集中在传统的V2X通信安全，而忽略了自然语言作为通信媒介引入的新型攻击方式，例如消息篡改、语义欺骗等。这些攻击可能导致车辆做出错误的决策，从而危及驾驶安全。

**核心思路**：论文的核心思路是构建一个全栈的安全防御体系，从连接层、内容层和决策层全面保护协同驾驶系统。通过引入语义防火墙过滤恶意信息，利用语言-感知一致性检查验证信息的真实性，并结合多源共识提高决策的鲁棒性。这种多层次的防御机制旨在应对各种类型的攻击，确保系统的安全可靠运行。

**技术框架**：SafeCoop的整体架构包含以下几个主要模块：1) **Agentic转换函数**：用于跨帧空间对齐，统一不同车辆的视角。2) **语义防火墙**：过滤掉明显不符合安全规则或包含恶意信息的通信内容。3) **语言-感知一致性检查**：验证接收到的自然语言描述与车辆自身感知到的环境信息是否一致，检测潜在的欺骗攻击。4) **多源共识**：综合多个车辆的信息，通过共识机制排除异常信息，提高决策的准确性和鲁棒性。

**关键创新**：该论文最重要的技术创新点在于提出了一个针对自然语言协同驾驶的全栈安全防御框架。与传统的安全方法不同，SafeCoop不仅关注连接安全，还深入到语义层面，通过语言理解和感知融合来检测和防御恶意攻击。此外，Agentic转换函数实现了跨车辆视角的对齐，为多源共识提供了基础。

**关键设计**：Agentic转换函数的设计细节未知，但推测可能涉及到坐标系转换、特征对齐等技术。语义防火墙可能基于预定义的规则或机器学习模型来识别恶意信息。语言-感知一致性检查可能使用自然语言处理技术提取语言描述的关键信息，并与车辆的感知结果进行匹配。多源共识的具体算法未知，但可能涉及到投票机制、贝叶斯推断等方法。

## 📊 实验亮点

SafeCoop在CARLA仿真环境中进行了全面的评估，结果表明，在恶意攻击下，SafeCoop能够将驾驶评分提高69.15%，同时恶意检测的F1分数达到67.32%。这些数据表明，SafeCoop能够有效地防御各种类型的攻击，显著提升了协同驾驶系统的安全性。

## 🎯 应用场景

该研究成果可应用于未来的智能交通系统，特别是自动驾驶车辆之间的协同驾驶场景。通过提高协同驾驶系统的安全性，可以减少交通事故，提高交通效率，并增强用户对自动驾驶技术的信任度。此外，该研究也为其他基于自然语言的人机协作系统提供了安全设计的参考。

## 📄 摘要（原文）

> Collaborative driving systems leverage vehicle-to-everything (V2X) communication across multiple agents to enhance driving safety and efficiency. Traditional V2X systems take raw sensor data, neural features, or perception results as communication media, which face persistent challenges, including high bandwidth demands, semantic loss, and interoperability issues. Recent advances investigate natural language as a promising medium, which can provide semantic richness, decision-level reasoning, and human-machine interoperability at significantly lower bandwidth. Despite great promise, this paradigm shift also introduces new vulnerabilities within language communication, including message loss, hallucinations, semantic manipulation, and adversarial attacks. In this work, we present the first systematic study of full-stack safety and security issues in natural-language-based collaborative driving. Specifically, we develop a comprehensive taxonomy of attack strategies, including connection disruption, relay/replay interference, content spoofing, and multi-connection forgery. To mitigate these risks, we introduce an agentic defense pipeline, which we call SafeCoop, that integrates a semantic firewall, language-perception consistency checks, and multi-source consensus, enabled by an agentic transformation function for cross-frame spatial alignment. We systematically evaluate SafeCoop in closed-loop CARLA simulation across 32 critical scenarios, achieving 69.15% driving score improvement under malicious attacks and up to 67.32% F1 score for malicious detection. This study provides guidance for advancing research on safe, secure, and trustworthy language-driven collaboration in transportation systems. Our project page is https://xiangbogaobarry.github.io/SafeCoop.

