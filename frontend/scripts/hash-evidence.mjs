import { createHash } from 'node:crypto';

const evidence = {
  riskScore: 94,
  riskLevel: 'HIGH',
  deepfakeProbability: 0.91,
  speakerSimilarity: 0.38,
  fraudIndicators: ['urgent_money_request', 'impersonation'],
  recommendation: 'VERIFY_CALLER',
};

const serializedEvidence = JSON.stringify(evidence);
const hash = createHash('sha256').update(serializedEvidence, 'utf8').digest('hex');

console.log(`Evidence JSON: ${serializedEvidence}`);
console.log(`SHA-256: ${hash}`);
