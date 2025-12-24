---
layout: default
title: A DeepSeek-Powered AI System for Automated Chest Radiograph Interpretation in Clinical Practice
---

# A DeepSeek-Powered AI System for Automated Chest Radiograph Interpretation in Clinical Practice

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20344" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20344v1</a>
  <a href="https://arxiv.org/pdf/2512.20344.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20344v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20344v1', 'A DeepSeek-Powered AI System for Automated Chest Radiograph Interpretation in Clinical Practice')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yaowei Bai, Ruiheng Zhang, Yu Lei, Xuhua Duan, Jingfeng Yao, Shuguang Ju, Chaoyang Wang, Wei Yao, Yiwan Guo, Guilin Zhang, Chao Wan, Qian Yuan, Lei Chen, Wenjuan Tang, Biqiang Zhu, Xinggang Wang, Tao Sun, Wei Zhou, Dacheng Tao, Yongchao Xu, Chuansheng Zheng, Huangxuan Zhao, Bo Du

**分类**: cs.AI

**发布日期**: 2025-12-23

**备注**: arXiv admin note: substantial text overlap with arXiv:2507.19493

---

## 💡 一句话要点

**DeepSeek赋能的AI系统Janus-Pro-CXR，用于临床胸部X光片自动判读**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `胸部X光片判读` `人工智能辅助诊断` `深度学习` `自然语言生成` `临床验证`

## 📋 核心要点

1. 放射科医生短缺和胸部X光片工作量大，尤其在基层医疗，对X光片判读提出了挑战。
2. Janus-Pro-CXR基于DeepSeek模型，通过领域优化，实现高效准确的胸部X光片判读。
3. 前瞻性临床试验表明，AI辅助提高了报告质量，缩短了判读时间，并受到专家青睐。

## 📝 摘要（中文）

由于放射科医生在全球范围内短缺，胸部X光片的工作量巨大，尤其是在基层医疗中。尽管多模态大型语言模型显示出前景，但现有的评估主要依赖于自动指标或回顾性分析，缺乏严格的前瞻性临床验证。我们开发了基于DeepSeek Janus-Pro模型的胸部X光片判读系统Janus-Pro-CXR (10亿参数)，并通过一项多中心前瞻性试验(NCT07117266)进行了严格验证。我们的系统在自动报告生成方面优于最先进的X光报告生成模型，甚至超过了更大规模的模型，包括ChatGPT 4o (2000亿参数)，同时证明了对六种临床关键放射学发现的可靠检测。回顾性评估证实，报告准确性显著高于Janus-Pro和ChatGPT 4o。在前瞻性临床部署中，AI辅助显著提高了报告质量评分，减少了18.3%的判读时间(P < 0.001)，并且在54.3%的案例中受到大多数专家的青睐。通过轻量级架构和领域特定的优化，Janus-Pro-CXR提高了诊断可靠性和工作流程效率，尤其是在资源受限的环境中。该模型架构和实现框架将开源，以促进AI辅助放射解决方案的临床转化。

## 🔬 方法详解

**问题定义**：论文旨在解决放射科医生短缺和胸部X光片判读工作量大的问题，尤其是在基层医疗中。现有方法，包括大型语言模型，虽然有潜力，但缺乏严格的前瞻性临床验证，且模型规模庞大，难以在资源受限的环境中部署。

**核心思路**：论文的核心思路是利用DeepSeek Janus-Pro模型，通过领域特定的优化和轻量级架构，构建一个高效、准确且易于部署的胸部X光片判读系统。该系统旨在提高诊断可靠性和工作流程效率，尤其是在资源受限的环境中。

**技术框架**：Janus-Pro-CXR系统的整体架构基于DeepSeek Janus-Pro模型，并针对胸部X光片判读任务进行了优化。具体流程包括：图像输入、特征提取、报告生成和临床验证。系统包含的关键模块包括：图像处理模块、自然语言生成模块和临床反馈模块。

**关键创新**：最重要的技术创新点在于领域特定的优化和轻量级架构。通过针对胸部X光片判读任务进行优化，Janus-Pro-CXR在保证准确性的前提下，显著降低了模型规模，使其更易于部署和应用。与现有方法相比，Janus-Pro-CXR在报告准确性和效率方面均有显著提升。

**关键设计**：论文中关于关键参数设置、损失函数和网络结构的具体技术细节未详细描述，属于未知信息。但可以推测，针对胸部X光片判读任务，可能采用了特定的损失函数来优化报告生成，并可能对网络结构进行了剪枝或蒸馏，以实现轻量化。

## 📊 实验亮点

Janus-Pro-CXR在自动报告生成方面优于最先进的X光报告生成模型，甚至超过了ChatGPT 4o (2000亿参数)。前瞻性临床部署中，AI辅助显著提高了报告质量评分，减少了18.3%的判读时间(P < 0.001)，并且在54.3%的案例中受到大多数专家的青睐。

## 🎯 应用场景

该研究成果可广泛应用于基层医疗机构、体检中心和远程医疗等场景，辅助医生进行胸部X光片的快速准确判读，提高诊断效率和质量，尤其是在放射科医生资源匮乏的地区。未来，该系统有望与电子病历系统集成，实现更智能化的医疗服务。

## 📄 摘要（原文）

> A global shortage of radiologists has been exacerbated by the significant volume of chest X-ray workloads, particularly in primary care. Although multimodal large language models show promise, existing evaluations predominantly rely on automated metrics or retrospective analyses, lacking rigorous prospective clinical validation. Janus-Pro-CXR (1B), a chest X-ray interpretation system based on DeepSeek Janus-Pro model, was developed and rigorously validated through a multicenter prospective trial (NCT07117266). Our system outperforms state-of-the-art X-ray report generation models in automated report generation, surpassing even larger-scale models including ChatGPT 4o (200B parameters), while demonstrating reliable detection of six clinically critical radiographic findings. Retrospective evaluation confirms significantly higher report accuracy than Janus-Pro and ChatGPT 4o. In prospective clinical deployment, AI assistance significantly improved report quality scores, reduced interpretation time by 18.3% (P < 0.001), and was preferred by a majority of experts in 54.3% of cases. Through lightweight architecture and domain-specific optimization, Janus-Pro-CXR improves diagnostic reliability and workflow efficiency, particularly in resource-constrained settings. The model architecture and implementation framework will be open-sourced to facilitate the clinical translation of AI-assisted radiology solutions.

