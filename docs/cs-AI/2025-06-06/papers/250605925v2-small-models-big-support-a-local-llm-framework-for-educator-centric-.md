---
layout: default
title: "Small Models, Big Support: A Local LLM Framework for Educator-Centric Content Creation and Assessment with RAG and CAG"
---

# Small Models, Big Support: A Local LLM Framework for Educator-Centric Content Creation and Assessment with RAG and CAG

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05925" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05925v2</a>
  <a href="https://arxiv.org/pdf/2506.05925.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05925v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05925v2', 'Small Models, Big Support: A Local LLM Framework for Educator-Centric Content Creation and Assessment with RAG and CAG')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zarreen Reza, Alexander Mazur, Michael T. Dugdale, Robin Ray-Chaudhuri

**分类**: cs.CY, cs.AI

**发布日期**: 2025-06-06 (更新: 2025-11-16)

---

## 💡 一句话要点

**提出小型LLM框架以支持教育者内容创作与评估**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `小型语言模型` `教育技术` `内容生成` `AI辅助评估` `本地部署` `开源框架` `教师参与` `检索增强生成`

## 📋 核心要点

1. 现有教育工具多依赖大型云端LLMs，导致成本高、隐私风险大，且缺乏对教育者的直接支持。
2. 提出一种开源框架，利用小型LLMs实现本地部署，支持教师定制教学材料和AI辅助评估。
3. 在大学物理课程中成功部署，验证了该框架的可行性，显示出小型LLMs在教育领域的实用性。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）在面向学生的教育工具中应用广泛，但其直接支持教育者的潜力仍未得到充分探索。现有方法多依赖于专有的云端系统，给教育机构带来了成本、隐私和控制等方面的担忧。为此，本文提出了一种端到端的开源框架，利用小型（3B-7B参数）可本地部署的LLMs，全面支持教师，包括定制教学材料生成和AI辅助评估。该框架结合了检索增强生成（RAG）和上下文增强生成（CAG），确保生成内容的事实准确性和教学风格。核心特性是教师参与的互动优化循环，确保教育者的主导权和最终输出的精确对齐。通过在大学物理课程中的技术部署验证了该框架的可行性，结果表明小型LLMs构建的自托管系统能够为教育者提供强大、经济且私密的支持。

## 🔬 方法详解

**问题定义**：论文旨在解决现有教育工具中大型云端LLMs对教育者支持不足的问题，尤其是在成本、隐私和控制方面的挑战。

**核心思路**：通过构建一个开源框架，利用小型LLMs实现本地部署，提供定制化的教学支持和评估功能，确保教育者能够直接参与内容生成过程。

**技术框架**：该框架包括两个主要模块：检索增强生成（RAG）和上下文增强生成（CAG），并通过教师参与的互动优化循环来提升内容质量和相关性。

**关键创新**：核心创新在于结合RAG和CAG技术，形成一个教师在环的机制，确保生成内容的准确性和教学适用性，这与传统的云端LLMs方法有本质区别。

**关键设计**：框架中设置了辅助验证LLM，负责检查所有生成内容的可靠性和安全性，确保最终输出符合教育标准。

## 📊 实验亮点

实验结果表明，该框架在大学物理课程中的应用成功，生成的教学内容在准确性和教学风格上均达到了预期效果，展示了小型LLMs在教育领域的强大潜力。与传统大型模型相比，该框架在成本和隐私保护方面具有显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括中小学及高等教育的教学支持系统，能够为教师提供个性化的教学材料和评估工具，提升教学效率和质量。未来，该框架有望在教育技术领域引领更多自主可控的AI工具开发，满足教育机构的实际需求。

## 📄 摘要（原文）

> While Large Language Models (LLMs) are increasingly applied in student-facing educational tools, their potential to directly support educators through locally deployable and customizable solutions remains underexplored. Many existing approaches rely on proprietary, cloud-based systems that raise significant cost, privacy, and control concerns for educational institutions. To address these barriers, we introduce an end-to-end, open-source framework that empowers educators using small (3B-7B parameter), locally deployable LLMs. Our system is designed for comprehensive teacher support, including customized teaching material generation and AI-assisted assessment. The framework synergistically combines Retrieval-Augmented Generation (RAG) and Context-Augmented Generation (CAG) to produce factually accurate, pedagogically-styled content. A core feature is an interactive refinement loop, a teacher-in-the-loop mechanism that ensures educator agency and precise alignment of the final output. To enhance reliability and safety, an auxiliary verifier LLM inspects all generated content. We validate our framework through a rigorous evaluation of its content generation capabilities and report on a successful technical deployment in a college physics course, which confirms its feasibility on standard institutional hardware. Our findings demonstrate that carefully engineered, self-hosted systems built on small LLMs can provide robust, affordable, and private support for educators, achieving practical utility comparable to much larger models for targeted instructional tasks. This work presents a practical blueprint for the development of sovereign AI tools tailored to the real-world needs of educational institutions.

