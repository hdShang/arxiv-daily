---
layout: default
title: In-Context Compositional Learning via Sparse Coding Transformer
---

# In-Context Compositional Learning via Sparse Coding Transformer

**arXiv**: [2511.20194v1](https://arxiv.org/abs/2511.20194) | [PDF](https://arxiv.org/pdf/2511.20194.pdf)

**作者**: Wei Chen, Jingxi Yu, Zichen Miao, Qiang Qiu

---

## 💡 一句话要点

**提出稀疏编码Transformer以增强Transformer在上下文组合学习中的能力**

**关键词**: `上下文组合学习` `稀疏编码` `Transformer架构` `注意力机制` `组合规则推断` `RAVEN数据集`

## 📋 核心要点

1. Transformer在组合学习任务中表现不佳，缺乏结构归纳偏置
2. 将注意力块重新解释为编码和解码字典，对系数施加稀疏性以捕捉组合结构
3. 在S-RAVEN和RAVEN数据集上验证，在标准Transformer失败时保持性能

## 📄 摘要（原文）

> Transformer architectures have achieved remarkable success across language, vision, and multimodal tasks, and there is growing demand for them to address in-context compositional learning tasks. In these tasks, models solve the target problems by inferring compositional rules from context examples, which are composed of basic components structured by underlying rules. However, some of these tasks remain challenging for Transformers, which are not inherently designed to handle compositional tasks and offer limited structural inductive bias. In this work, inspired by the principle of sparse coding, we propose a reformulation of the attention to enhance its capability for compositional tasks. In sparse coding, data are represented as sparse combinations of dictionary atoms with coefficients that capture their compositional rules. Specifically, we reinterpret the attention block as a mapping of inputs into outputs through projections onto two sets of learned dictionary atoms: an encoding dictionary and a decoding dictionary. The encoding dictionary decomposes the input into a set of coefficients, which represent the compositional structure of the input. To enhance structured representations, we impose sparsity on these coefficients. The sparse coefficients are then used to linearly combine the decoding dictionary atoms to generate the output. Furthermore, to assist compositional generalization tasks, we propose estimating the coefficients of the target problem as a linear combination of the coefficients obtained from the context examples. We demonstrate the effectiveness of our approach on the S-RAVEN and RAVEN datasets. For certain compositional generalization tasks, our method maintains performance even when standard Transformers fail, owing to its ability to learn and apply compositional rules.

